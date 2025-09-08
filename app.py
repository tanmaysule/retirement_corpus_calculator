from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, model_validator
from typing import List, Dict, Optional
import uvicorn
from recurring_investment import RecurringInvestment, CompoundingType, InvestmentType
from retirement_withdrawal import RetirementWithdrawal

app = FastAPI(title="Retirement Corpus Calculator")

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class InvestmentModel(BaseModel):
    id: int = Field(..., description="Unique identifier for the investment model")
    name: str = Field(..., description="User-defined name for the investment model")
    base_amount: float = Field(..., description="Initial investment amount")
    recurring_amount: float = Field(..., description="Recurring investment amount (monthly for MoM, yearly for YoY/YoM)")
    step_up_rate: float = Field(..., description="Annual step up rate percentage")
    avg_growth_rate: float = Field(..., description="Expected annual growth rate percentage") 
    investment_model: str = Field(..., description="Investment model type: mom, yoy, or yom")

class CalculationRequest(BaseModel):
    # Investment parameters
    investment_year: int = Field(..., description="The year when investments start")
    investment_models: List[InvestmentModel] = Field(..., description="List of investment models", min_length=1, max_length=10)
    
    # Retirement parameters
    current_age: int = Field(..., description="Current age of the user")
    retirement_age: int = Field(..., description="Expected retirement age")
    expected_life_span: int = Field(..., description="Expected life span")
    retirement_corpus_manual: Optional[float] = Field(None, description="Manual override for retirement corpus")
    inflation_rate: float = Field(..., description="Expected inflation rate percentage")
    post_retirement_return_rate: Optional[float] = Field(default=0.0, description="Expected return rate during retirement")
    yearly_withdrawal: float = Field(..., description="Yearly withdrawal amount in today's money")
    
    # Display parameters
    years_to_display: int = Field(..., description="Number of years to display in chart")

    @model_validator(mode='after')
    def validate_age_relationships(self) -> 'CalculationRequest':
        if self.retirement_age <= self.current_age:
            raise ValueError("Retirement age must be greater than current age")
        
        if self.expected_life_span <= self.retirement_age:
            raise ValueError("Expected life span must be greater than retirement age")
        
        return self

@app.get("/")
async def home(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate_retirement_journey(calculation_request: CalculationRequest) -> Dict:
    """Calculate complete retirement journey with multiple investment models"""
    
    try:
        # Calculate retirement year from retirement age
        retirement_year = calculation_request.investment_year + (calculation_request.retirement_age - calculation_request.current_age)
        
        # Helper function to map investment model types
        def get_investment_types(model_type: str):
            if model_type == "mom":
                return CompoundingType.MONTHLY, InvestmentType.MONTHLY
            elif model_type == "yoy":
                return CompoundingType.YEARLY, InvestmentType.YEARLY
            elif model_type == "yom":
                return CompoundingType.MONTHLY, InvestmentType.YEARLY
            else:
                raise ValueError(f"Invalid investment model: {model_type}")
        
        # Phase 1: Create multiple investment models
        investments = []
        for model_data in calculation_request.investment_models:
            compounding_type, investment_type = get_investment_types(model_data.investment_model)
            
            investment = RecurringInvestment(
                base_amount=model_data.base_amount,
                recurring_amount=model_data.recurring_amount,
                step_up_rate=model_data.step_up_rate,
                avg_growth_rate=model_data.avg_growth_rate,
                investment_year=calculation_request.investment_year,
                compounding_type=compounding_type,
                investment_type=investment_type
            )
            investments.append({
                "id": model_data.id,
                "name": model_data.name,
                "investment": investment
            })
        
        # Calculate total retirement corpus
        if calculation_request.retirement_corpus_manual is not None and calculation_request.retirement_corpus_manual > 0:
            retirement_corpus = calculation_request.retirement_corpus_manual
            corpus_source = "manual"
        else:
            # Sum all investment models at retirement year
            retirement_corpus = sum(inv["investment"].calculate_amount(retirement_year) for inv in investments)
            corpus_source = "calculated"
        
        # Phase 2: Retirement Withdrawal Phase  
        withdrawal = RetirementWithdrawal(
            retirement_corpus=retirement_corpus,
            current_age=calculation_request.current_age,
            current_year=calculation_request.investment_year,
            retirement_year=retirement_year,
            expected_life_span=calculation_request.expected_life_span,
            inflation_rate=calculation_request.inflation_rate,
            post_retirement_return_rate=calculation_request.post_retirement_return_rate,
            yearly_withdrawal=calculation_request.yearly_withdrawal
        )
        
        # Generate data for charts
        years = []
        investment_data = {}  # {model_id: [amounts]}
        total_investment_data = []  # Combined amounts
        retirement_data = []  # Retirement phase amounts
        phases = []
        
        # Initialize investment data structure
        for inv in investments:
            investment_data[inv["id"]] = []
        
        # Investment phase: from start year to retirement year
        for year in range(calculation_request.investment_year, retirement_year + 1):
            years.append(year)
            phases.append("investment")
            
            # Calculate each investment model separately
            total_amount = 0
            for inv in investments:
                amount = inv["investment"].calculate_amount(year)
                investment_data[inv["id"]].append(round(amount, 2))
                total_amount += amount
            
            total_investment_data.append(round(total_amount, 2))
            retirement_data.append(None)  # No retirement data during investment phase
        
        # Retirement phase: from retirement year to end of display period
        end_year = calculation_request.investment_year + calculation_request.years_to_display
        max_retirement_year = retirement_year + (calculation_request.expected_life_span - calculation_request.retirement_age)
        
        for year in range(retirement_year + 1, min(end_year + 1, max_retirement_year + 1)):
            try:
                remaining_corpus = withdrawal.calculate_remaining_corpus(year)
                years.append(year)
                phases.append("retirement")
                
                # No new investment data during retirement
                for inv in investments:
                    investment_data[inv["id"]].append(None)
                total_investment_data.append(None)
                retirement_data.append(round(remaining_corpus, 2))
                
            except ValueError as e:
                # Corpus depleted - add one final point at zero
                if "depleted" in str(e).lower():
                    years.append(year)
                    phases.append("depleted")
                    
                    for inv in investments:
                        investment_data[inv["id"]].append(None)
                    total_investment_data.append(None)
                    retirement_data.append(0)
                    break
        
        # Calculate total corpus at retirement for reference
        calculated_total_corpus = sum(inv["investment"].calculate_amount(retirement_year) for inv in investments)
        
        # Prepare investment model summaries for frontend
        investment_summaries = []
        for inv in investments:
            corpus_at_retirement = inv["investment"].calculate_amount(retirement_year)
            investment_summaries.append({
                "id": inv["id"],
                "name": inv["name"],
                "corpus_at_retirement": round(corpus_at_retirement, 2),
                "model_type": next(m.investment_model for m in calculation_request.investment_models if m.id == inv["id"])
            })
        
        return {
            "years": years,
            "phases": phases,
            "investment_data": investment_data,  # Individual model data
            "total_investment_data": total_investment_data,  # Combined investment data
            "retirement_data": retirement_data,  # Retirement phase data
            "investment_summaries": investment_summaries,  # Model summaries
            "retirement_corpus": round(retirement_corpus, 2),
            "calculated_total_corpus": round(calculated_total_corpus, 2),
            "corpus_source": corpus_source,
            "retirement_year": retirement_year,
            "retirement_age": calculation_request.retirement_age,
            "success": True,
            "message": f"Successfully calculated multi-investment retirement journey. Total corpus: ₹{retirement_corpus:,.2f} ({corpus_source})"
        }
        
    except ValueError as e:
        # Handle validation errors from our models
        raise HTTPException(status_code=400, detail=str(e))
        
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=f"Calculation error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
