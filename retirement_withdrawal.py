import glog as log
from enum import Enum

from pydantic import BaseModel, Field


class RetirementWithdrawal(BaseModel):
    retirement_corpus: float = Field(..., description="The corpus amount accumulated before retirement")

    current_age: int = Field(..., description="Current age")
    current_year: int = Field(..., description="The current year (expected that you will be working in this year)")
    retirement_year: int = Field(..., description="The year of retirement (expected that you will retire at the start of this year)")
    expected_life_span: int = Field(..., description="Expected life span in terms of age")

    inflation_rate: float = Field(..., description="Average inflation rate in percentage")
    yearly_withdrawal: float = Field(..., description="The yearly withdrawal amount with respect to current year")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._validate_inputs()

    def _validate_inputs(self):
        """Comprehensive validation of all input parameters"""
        
        # Year validations
        if self.current_year > self.retirement_year:
            raise ValueError(f"Current year {self.current_year} cannot be greater than retirement year {self.retirement_year}")
        
        if self.current_year < 1900 or self.current_year > 2150:
            raise ValueError(f"Current year {self.current_year} must be between 1900 and 2150")
        
        if self.retirement_year < 1900 or self.retirement_year > 2150:
            raise ValueError(f"Retirement year {self.retirement_year} must be between 1900 and 2150")

        # Age validations
        if self.current_age < 18 or self.current_age > 100:
            raise ValueError(f"Current age {self.current_age} must be between 18 and 100 years")
        
        if self.expected_life_span < 30 or self.expected_life_span > 120:
            raise ValueError(f"Expected life span {self.expected_life_span} must be between 30 and 120 years")
        
        if self.expected_life_span <= self.current_age:
            raise ValueError(f"Expected life span {self.expected_life_span} must be greater than current age {self.current_age}")

        # Age and year consistency validations
        retirement_age = self.current_age + (self.retirement_year - self.current_year)
        if retirement_age < 40 or retirement_age > 85:
            raise ValueError(f"Retirement age {retirement_age} must be between 40 and 85 years")
        
        if retirement_age >= self.expected_life_span:
            raise ValueError(f"Retirement age {retirement_age} must be less than expected life span {self.expected_life_span}")

        # Financial validations
        if self.retirement_corpus <= 0:
            raise ValueError(f"Retirement corpus {self.retirement_corpus} must be positive")
        
        if self.retirement_corpus < 100000:  # Minimum 1 lakh corpus
            raise ValueError(f"Retirement corpus {self.retirement_corpus} seems too small for retirement (minimum 1,00,000)")
        
        if self.yearly_withdrawal <= 0:
            raise ValueError(f"Yearly withdrawal {self.yearly_withdrawal} must be positive")
        
        if self.inflation_rate < -10 or self.inflation_rate > 50:
            raise ValueError(f"Inflation rate {self.inflation_rate}% must be between -10% and 50%")

        # Logical sustainability validations
        years_in_retirement = self.expected_life_span - retirement_age
        if years_in_retirement < 5:
            raise ValueError(f"Years in retirement ({years_in_retirement}) must be at least 5 years")
        
        # Check if withdrawal rate is reasonable (not more than 10% of corpus initially)
        withdrawal_rate = (self.yearly_withdrawal / self.retirement_corpus) * 100
        if withdrawal_rate > 10:
            raise ValueError(f"Initial withdrawal rate {withdrawal_rate:.1f}% is too high (recommended maximum: 10% of corpus)")
        
        # Basic sustainability check - ensure corpus can last at least 10 years with inflation
        inflated_first_year_withdrawal = self.yearly_withdrawal * (1 + self.inflation_rate/100) ** (self.retirement_year - self.current_year)
        if inflated_first_year_withdrawal * 10 > self.retirement_corpus:
            raise ValueError(f"Withdrawal amount is too high - corpus may not last even 10 years")


    def calculate_remaining_corpus(self, year: int):
        """
        Calculate the remaining corpus at the end of the given year.

        Args:
            year: Year for which the remaining corpus is to be calculated

        Returns:
            Remaining corpus at the end of the given year
        """

        if year < self.current_year or year < self.retirement_year:
            raise ValueError(f"Cannot calculate remaining corpus for year {year} before current year {self.current_year} or retirement year {self.retirement_year}")
        
        remaining_corpus = self.retirement_corpus
        amount_to_spend = self.yearly_withdrawal * (1 + self.inflation_rate/100) ** (self.retirement_year - self.current_year)
        for year in range(self.retirement_year, year + 1):
            """
            Period's start: Remove the amount to spend this year
            """
            remaining_corpus = remaining_corpus - amount_to_spend
            if(remaining_corpus < 0):
                raise ValueError(f"Remaining corpus cannot be negative for year {year}")

            """
            Period's end: Add the inflation for this period
            """
            amount_to_spend = amount_to_spend * (1 + self.inflation_rate/100)
        
        return remaining_corpus

        