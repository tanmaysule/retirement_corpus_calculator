from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict
import uvicorn
from recurring_investment import RecurringInvestment, CompoundingType, InvestmentType

app = FastAPI(title="Retirement Corpus Calculator")

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class CalculationRequest(BaseModel):
    base_amount: float
    recurring_amount: float
    step_up_rate: float
    avg_growth_rate: float
    investment_year: int
    compounding_type: str
    investment_type: str
    years_to_calculate: int

@app.get("/")
async def home(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate")
async def calculate_investment(calculation_request: CalculationRequest) -> Dict[str, List]:
    """Calculate investment amounts for the specified years"""
    
    # Convert string enums to actual enum values
    compounding_type = CompoundingType.MONTHLY if calculation_request.compounding_type == "monthly" else CompoundingType.YEARLY
    investment_type = InvestmentType.MONTHLY if calculation_request.investment_type == "monthly" else InvestmentType.YEARLY
    
    # Create RecurringInvestment instance
    investment = RecurringInvestment(
        base_amount=calculation_request.base_amount,
        recurring_amount=calculation_request.recurring_amount,
        step_up_rate=calculation_request.step_up_rate,
        avg_growth_rate=calculation_request.avg_growth_rate,
        investment_year=calculation_request.investment_year,
        compounding_type=compounding_type,
        investment_type=investment_type
    )
    
    # Calculate amounts for each year
    years = []
    amounts = []
    
    for i in range(calculation_request.years_to_calculate):
        year = calculation_request.investment_year + i
        amount = investment.calculate_amount(year)
        years.append(year)
        amounts.append(round(amount, 2))
    
    return {"years": years, "amounts": amounts}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
