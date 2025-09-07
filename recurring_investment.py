import glog as log
from enum import Enum

from pydantic import BaseModel, Field

class BulkInvestment(BaseModel):
    amount: float = Field(..., description="The amount of the investment")
    avg_growth_rate: float = Field(..., description="The average growth rate of the investment in percentage")
    investment_year: int = Field(..., description="The year of the investment. The amount was invested in this year's start")


    def calculate_amount(self, year: int):
        """
        Calculate the amount of the investment after at given year's END.

        Args:
            year: Year for which the amount is to be calculated

        Returns:
            Amount of the investment at the specified year's end
        """
        if year < self.investment_year:
            raise ValueError(f"Cannot calculate amount for year {year} before investment start year {self.investment_year}")
        
        return self.amount * (1 + self.avg_growth_rate/100) ** (year - self.investment_year + 1)

class CompoundingType(Enum):
    MONTHLY = "monthly"
    YEARLY = "yearly"

class InvestmentType(Enum):
    MONTHLY = "monthly"
    YEARLY = "yearly"    

class RecurringInvestment(BaseModel):
    base_amount: float = Field(..., description="The initial starting amount for the investment")
    recurring_amount: float = Field(..., description="The monthly investment amount (for yearly investments, this gets multiplied by 12)")
    step_up_rate: float = Field(..., description="The step up rate of the investment per year in percentage")
    avg_growth_rate: float = Field(..., description="The average growth rate of the investment in percentage per year")
    investment_year: int = Field(..., description="The year of the investment. The investment was started in this year's start")
    compounding_type: CompoundingType = Field(..., description="Whether the investment is compounded monthly or yearly")
    investment_type: InvestmentType = Field(..., description="Whether the investment of the amount is done monthly or yearly")

    def calculate_amount(self, year: int):
        """
        Calculate the amount of the investment after at given year's END.

        Args:
            year: Year for which the amount is to be calculated

        Returns:
            Amount of the investment at the specified year's end

        Note:
            Investments are done at the start of each month or year.
            i.e. 1st of each month or 1 Jan each year
        """
        if year < self.investment_year:
            raise ValueError(f"Cannot calculate amount for year {year} before investment start year {self.investment_year}")
        
        total_amount = self.base_amount
        amount_to_invest = self.recurring_amount if self.investment_type == InvestmentType.MONTHLY else self.recurring_amount * 12

        if self.compounding_type == CompoundingType.MONTHLY:
            rate = (1 + self.avg_growth_rate/100) ** (1/12) - 1
        else:
            rate = self.avg_growth_rate/100

        for month in range((year - self.investment_year + 1) * 12):
            """
            Period's start: Add the investment for this period
            """
            if self.investment_type == InvestmentType.MONTHLY or month % 12 == 0:
                total_amount = total_amount + amount_to_invest

            """
            Period's End: Add the interest for this period
            """
            if self.compounding_type == CompoundingType.MONTHLY or month % 12 == 11:
                total_amount = total_amount * (1 + rate)


            if (month + 1) % 12 == 0:
                """
                Increase the investment for the next year
                """
                amount_to_invest = amount_to_invest * (1 + self.step_up_rate/100)
        
        return total_amount


def main():
    recurring_investment = RecurringInvestment(
        base_amount = 1_00_000,
        recurring_amount = 0,
        step_up_rate = 5,
        avg_growth_rate = 12,
        investment_year = 2025,
        compounding_type = CompoundingType.YEARLY,
        investment_type = InvestmentType.YEARLY
    )

    for year in range(2025, 2055):
        log.info(f"Amount at Year {year}'s end: {recurring_investment.calculate_amount(year)}")


if __name__ == "__main__":
    main()
