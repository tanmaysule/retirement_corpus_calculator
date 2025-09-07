from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
from recurring_investment import RecurringInvestment, CompoundingType, InvestmentType
from retirement_withdrawal import RetirementWithdrawal

app = FastAPI(title="Retirement Corpus Calculator")

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class CalculationRequest(BaseModel):
    # Investment parameters
    base_amount: float
    recurring_amount: float
    step_up_rate: float
    avg_growth_rate: float
    investment_year: int
    compounding_type: str
    investment_type: str
    
    # Retirement parameters
    retirement_year: int
    current_age: int
    expected_life_span: int
    inflation_rate: float
    post_retirement_return_rate: Optional[float] = 0.0
    yearly_withdrawal: float
    
    # Display parameters
    years_to_display: int

@app.get("/")
async def home(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate_retirement_journey(calculation_request: CalculationRequest) -> Dict:
    """Calculate complete retirement journey: investment accumulation + withdrawal phase"""
    
    try:
        # Phase 1: Investment Accumulation Phase
        compounding_type = CompoundingType.MONTHLY if calculation_request.compounding_type == "monthly" else CompoundingType.YEARLY
        investment_type = InvestmentType.MONTHLY if calculation_request.investment_type == "monthly" else InvestmentType.YEARLY
        
        investment = RecurringInvestment(
            base_amount=calculation_request.base_amount,
            recurring_amount=calculation_request.recurring_amount,
            step_up_rate=calculation_request.step_up_rate,
            avg_growth_rate=calculation_request.avg_growth_rate,
            investment_year=calculation_request.investment_year,
            compounding_type=compounding_type,
            investment_type=investment_type
        )
        
        # Calculate retirement corpus (amount at retirement year)
        retirement_corpus = investment.calculate_amount(calculation_request.retirement_year)
        
        # Phase 2: Retirement Withdrawal Phase  
        withdrawal = RetirementWithdrawal(
            retirement_corpus=retirement_corpus,
            current_age=calculation_request.current_age,
            current_year=calculation_request.investment_year,  # Use investment start year as current year
            retirement_year=calculation_request.retirement_year,
            expected_life_span=calculation_request.expected_life_span,
            inflation_rate=calculation_request.inflation_rate,
            post_retirement_return_rate=calculation_request.post_retirement_return_rate,
            yearly_withdrawal=calculation_request.yearly_withdrawal
        )
        
        # Combine both phases for the graph
        years = []
        amounts = []
        phases = []  # Track which phase each point belongs to
        
        # Investment phase: from start year to retirement year
        for year in range(calculation_request.investment_year, calculation_request.retirement_year + 1):
            years.append(year)
            amount = investment.calculate_amount(year)
            amounts.append(round(amount, 2))
            phases.append("investment")
        
        # Retirement phase: from retirement year to end of display period
        end_year = calculation_request.investment_year + calculation_request.years_to_display
        retirement_age_at_start = calculation_request.current_age + (calculation_request.retirement_year - calculation_request.investment_year)
        
        for year in range(calculation_request.retirement_year + 1, min(end_year + 1, calculation_request.retirement_year + (calculation_request.expected_life_span - retirement_age_at_start) + 1)):
            try:
                remaining_corpus = withdrawal.calculate_remaining_corpus(year)
                years.append(year)
                amounts.append(round(remaining_corpus, 2))
                phases.append("retirement")
            except ValueError as e:
                # Corpus depleted - add one final point at zero
                if "depleted" in str(e).lower():
                    years.append(year)
                    amounts.append(0)
                    phases.append("depleted")
                    break
        
        return {
            "years": years,
            "amounts": amounts,
            "phases": phases,
            "retirement_corpus": round(retirement_corpus, 2),
            "retirement_year": calculation_request.retirement_year,
            "success": True,
            "message": f"Successfully calculated retirement journey. Retirement corpus: ₹{retirement_corpus:,.2f}"
        }
        
    except ValueError as e:
        # Handle validation errors from our models
        raise HTTPException(status_code=400, detail=str(e))
        
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=f"Calculation error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
