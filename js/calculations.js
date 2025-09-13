// JavaScript equivalent of the Python calculation classes

// Enums
const CompoundingType = {
    MONTHLY: "monthly",
    YEARLY: "yearly"
};

const InvestmentType = {
    MONTHLY: "monthly",
    YEARLY: "yearly"
};

class RecurringInvestment {
    constructor({
        base_amount,
        recurring_amount,
        step_up_rate,
        avg_growth_rate,
        investment_year,
        compounding_type,
        investment_type
    }) {
        this.base_amount = base_amount;
        this.recurring_amount = recurring_amount;
        this.step_up_rate = step_up_rate;
        this.avg_growth_rate = avg_growth_rate;
        this.investment_year = investment_year;
        this.compounding_type = compounding_type;
        this.investment_type = investment_type;
    }

    calculateAmount(year) {
        if (year < this.investment_year) {
            throw new Error(`Cannot calculate amount for year ${year} before investment start year ${this.investment_year}`);
        }
        
        let total_amount = this.base_amount;
        let amount_to_invest = this.investment_type === InvestmentType.MONTHLY 
            ? this.recurring_amount 
            : this.recurring_amount * 12;

        let rate;
        if (this.compounding_type === CompoundingType.MONTHLY) {
            rate = Math.pow(1 + this.avg_growth_rate/100, 1/12) - 1;
        } else {
            rate = this.avg_growth_rate/100;
        }

        const totalMonths = (year - this.investment_year + 1) * 12;
        
        for (let month = 0; month < totalMonths; month++) {
            // Period's start: Add the investment for this period
            if (this.investment_type === InvestmentType.MONTHLY || month % 12 === 0) {
                total_amount = total_amount + amount_to_invest;
            }

            // Period's End: Add the interest for this period
            if (this.compounding_type === CompoundingType.MONTHLY || month % 12 === 11) {
                total_amount = total_amount * (1 + rate);
            }

            if ((month + 1) % 12 === 0) {
                // Increase the investment for the next year
                amount_to_invest = amount_to_invest * (1 + this.step_up_rate/100);
            }
        }
        
        return total_amount;
    }
}

class RetirementWithdrawal {
    constructor({
        retirement_corpus,
        current_age,
        current_year,
        retirement_year,
        expected_life_span,
        inflation_rate,
        post_retirement_return_rate = 0.0,
        yearly_withdrawal
    }) {
        this.retirement_corpus = retirement_corpus;
        this.current_age = current_age;
        this.current_year = current_year;
        this.retirement_year = retirement_year;
        this.expected_life_span = expected_life_span;
        this.inflation_rate = inflation_rate;
        this.post_retirement_return_rate = post_retirement_return_rate;
        this.yearly_withdrawal = yearly_withdrawal;
        
        this._validateInputs();
    }

    _validateInputs() {
        // Year validations
        if (this.current_year > this.retirement_year) {
            throw new Error(`Current year ${this.current_year} cannot be greater than retirement year ${this.retirement_year}`);
        }
        
        if (this.current_year < 1900 || this.current_year > 2150) {
            throw new Error(`Current year ${this.current_year} must be between 1900 and 2150`);
        }
        
        if (this.retirement_year < 1900 || this.retirement_year > 2150) {
            throw new Error(`Retirement year ${this.retirement_year} must be between 1900 and 2150`);
        }

        // Age validations
        if (this.current_age < 18 || this.current_age > 100) {
            throw new Error(`Current age ${this.current_age} must be between 18 and 100 years`);
        }
        
        if (this.expected_life_span < 30 || this.expected_life_span > 120) {
            throw new Error(`Expected life span ${this.expected_life_span} must be between 30 and 120 years`);
        }
        
        if (this.expected_life_span <= this.current_age) {
            throw new Error(`Expected life span ${this.expected_life_span} must be greater than current age ${this.current_age}`);
        }

        // Age and year consistency validations
        const retirement_age = this.current_age + (this.retirement_year - this.current_year);
        if (retirement_age < 40 || retirement_age > 85) {
            throw new Error(`Retirement age ${retirement_age} must be between 40 and 85 years`);
        }
        
        if (retirement_age >= this.expected_life_span) {
            throw new Error(`Retirement age ${retirement_age} must be less than expected life span ${this.expected_life_span}`);
        }

        // Financial validations
        if (this.retirement_corpus <= 0) {
            throw new Error(`Retirement corpus ${this.retirement_corpus} must be positive`);
        }
        
        if (this.retirement_corpus < 100000) {
            throw new Error(`Retirement corpus ${this.retirement_corpus} seems too small for retirement (minimum 1,00,000)`);
        }
        
        if (this.yearly_withdrawal <= 0) {
            throw new Error(`Yearly withdrawal ${this.yearly_withdrawal} must be positive`);
        }
        
        if (this.inflation_rate < -10 || this.inflation_rate > 50) {
            throw new Error(`Inflation rate ${this.inflation_rate}% must be between -10% and 50%`);
        }
        
        if (this.post_retirement_return_rate < -10 || this.post_retirement_return_rate > 30) {
            throw new Error(`Post-retirement return rate ${this.post_retirement_return_rate}% must be between -10% and 30%`);
        }

        // Logical sustainability validations
        const years_in_retirement = this.expected_life_span - retirement_age;
        if (years_in_retirement < 5) {
            throw new Error(`Years in retirement (${years_in_retirement}) must be at least 5 years`);
        }
        
        // Check if withdrawal rate is reasonable (not more than 10% of corpus initially)
        const withdrawal_rate = (this.yearly_withdrawal / this.retirement_corpus) * 100;
        if (withdrawal_rate > 10) {
            throw new Error(`Initial withdrawal rate ${withdrawal_rate.toFixed(1)}% is too high (recommended maximum: 10% of corpus)`);
        }
        
        // Basic sustainability check - ensure corpus can last at least 10 years with inflation
        const inflated_first_year_withdrawal = this.yearly_withdrawal * Math.pow(1 + this.inflation_rate/100, this.retirement_year - this.current_year);
        if (inflated_first_year_withdrawal * 10 > this.retirement_corpus) {
            throw new Error("Withdrawal amount is too high - corpus may not last even 10 years");
        }
    }

    calculateRemainingCorpus(target_year) {
        // Validation: Can only calculate for years during or after retirement
        if (target_year < this.retirement_year) {
            throw new Error(`Cannot calculate remaining corpus for year ${target_year} before retirement year ${this.retirement_year}`);
        }
        
        let remaining_corpus = this.retirement_corpus;
        
        // Calculate the withdrawal amount for the first retirement year (adjusted for inflation from current year)
        let amount_to_spend = this.yearly_withdrawal * Math.pow(1 + this.inflation_rate/100, this.retirement_year - this.current_year);
        
        // Simulate each year from retirement to target year
        for (let current_retirement_year = this.retirement_year; current_retirement_year <= target_year; current_retirement_year++) {
            // Beginning of year: Remove the amount to spend this year
            remaining_corpus = remaining_corpus - amount_to_spend;
            
            if (remaining_corpus < 0) {
                throw new Error(`Corpus depleted in year ${current_retirement_year}. Remaining corpus became negative: ₹${remaining_corpus.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2})}`);
            }

            // During the year: Apply post-retirement investment returns to remaining corpus
            remaining_corpus = remaining_corpus * (1 + this.post_retirement_return_rate/100);

            // End of year: Increase spending amount for next year due to inflation
            amount_to_spend = amount_to_spend * (1 + this.inflation_rate/100);
        }
        
        return remaining_corpus;
    }
}

// Helper function to map investment model types
function getInvestmentTypes(modelType) {
    if (modelType === "mom") {
        return [CompoundingType.MONTHLY, InvestmentType.MONTHLY];
    } else if (modelType === "yoy") {
        return [CompoundingType.YEARLY, InvestmentType.YEARLY];
    } else if (modelType === "yom") {
        return [CompoundingType.MONTHLY, InvestmentType.YEARLY];
    } else {
        throw new Error(`Invalid investment model: ${modelType}`);
    }
}

// Main calculation function - JavaScript equivalent of the FastAPI endpoint
function calculateRetirementJourney(calculationRequest) {
    try {
        // Calculate retirement year from retirement age
        const retirement_year = calculationRequest.investment_year + (calculationRequest.retirement_age - calculationRequest.current_age);
        
        // Phase 1: Create multiple investment models
        const investments = [];
        for (const modelData of calculationRequest.investment_models) {
            const [compounding_type, investment_type] = getInvestmentTypes(modelData.investment_model);
            
            const investment = new RecurringInvestment({
                base_amount: modelData.base_amount,
                recurring_amount: modelData.recurring_amount,
                step_up_rate: modelData.step_up_rate,
                avg_growth_rate: modelData.avg_growth_rate,
                investment_year: calculationRequest.investment_year,
                compounding_type: compounding_type,
                investment_type: investment_type
            });
            
            investments.push({
                id: modelData.id,
                name: modelData.name,
                investment: investment
            });
        }
        
        // Calculate total retirement corpus
        let retirement_corpus, corpus_source;
        if (calculationRequest.retirement_corpus_manual !== null && calculationRequest.retirement_corpus_manual > 0) {
            retirement_corpus = calculationRequest.retirement_corpus_manual;
            corpus_source = "manual";
        } else {
            // Sum all investment models at retirement year
            retirement_corpus = investments.reduce((sum, inv) => sum + inv.investment.calculateAmount(retirement_year), 0);
            corpus_source = "calculated";
        }
        
        // Phase 2: Retirement Withdrawal Phase  
        const withdrawal = new RetirementWithdrawal({
            retirement_corpus: retirement_corpus,
            current_age: calculationRequest.current_age,
            current_year: calculationRequest.investment_year,
            retirement_year: retirement_year,
            expected_life_span: calculationRequest.expected_life_span,
            inflation_rate: calculationRequest.inflation_rate,
            post_retirement_return_rate: calculationRequest.post_retirement_return_rate,
            yearly_withdrawal: calculationRequest.yearly_withdrawal
        });
        
        // Generate data for charts
        const years = [];
        const investment_data = {}; // {model_id: [amounts]}
        const total_investment_data = []; // Combined amounts
        const retirement_data = []; // Retirement phase amounts
        const phases = [];
        
        // Initialize investment data structure
        for (const inv of investments) {
            investment_data[inv.id] = [];
        }
        
        // Investment phase: from start year to retirement year
        for (let year = calculationRequest.investment_year; year <= retirement_year; year++) {
            years.push(year);
            phases.push("investment");
            
            // Calculate each investment model separately
            let total_amount = 0;
            for (const inv of investments) {
                const amount = inv.investment.calculateAmount(year);
                investment_data[inv.id].push(Math.round(amount * 100) / 100);
                total_amount += amount;
            }
            
            total_investment_data.push(Math.round(total_amount * 100) / 100);
            retirement_data.push(null); // No retirement data during investment phase
        }
        
        // Retirement phase: from retirement year to end of display period
        const end_year = calculationRequest.investment_year + calculationRequest.years_to_display;
        const max_retirement_year = retirement_year + (calculationRequest.expected_life_span - calculationRequest.retirement_age);
        
        for (let year = retirement_year + 1; year <= Math.min(end_year, max_retirement_year); year++) {
            try {
                const remaining_corpus = withdrawal.calculateRemainingCorpus(year);
                years.push(year);
                phases.push("retirement");
                
                // No new investment data during retirement
                for (const inv of investments) {
                    investment_data[inv.id].push(null);
                }
                total_investment_data.push(null);
                retirement_data.push(Math.round(remaining_corpus * 100) / 100);
                
            } catch (error) {
                // Corpus depleted - add one final point at zero
                if (error.message.toLowerCase().includes("depleted")) {
                    years.push(year);
                    phases.push("depleted");
                    
                    for (const inv of investments) {
                        investment_data[inv.id].push(null);
                    }
                    total_investment_data.push(null);
                    retirement_data.push(0);
                    break;
                }
                throw error; // Re-throw if it's not a depletion error
            }
        }
        
        // Calculate total corpus at retirement for reference
        const calculated_total_corpus = investments.reduce((sum, inv) => sum + inv.investment.calculateAmount(retirement_year), 0);
        
        // Prepare investment model summaries for frontend
        const investment_summaries = [];
        for (const inv of investments) {
            const corpus_at_retirement = inv.investment.calculateAmount(retirement_year);
            const model_data = calculationRequest.investment_models.find(m => m.id === inv.id);
            investment_summaries.push({
                id: inv.id,
                name: inv.name,
                corpus_at_retirement: Math.round(corpus_at_retirement * 100) / 100,
                model_type: model_data.investment_model
            });
        }
        
        return {
            years: years,
            phases: phases,
            investment_data: investment_data, // Individual model data
            total_investment_data: total_investment_data, // Combined investment data
            retirement_data: retirement_data, // Retirement phase data
            investment_summaries: investment_summaries, // Model summaries
            retirement_corpus: Math.round(retirement_corpus * 100) / 100,
            calculated_total_corpus: Math.round(calculated_total_corpus * 100) / 100,
            corpus_source: corpus_source,
            retirement_year: retirement_year,
            retirement_age: calculationRequest.retirement_age,
            success: true,
            message: `Successfully calculated multi-investment retirement journey. Total corpus: ₹${retirement_corpus.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2})} (${corpus_source})`
        };
        
    } catch (error) {
        // Handle validation errors from our models
        throw new Error(error.message);
    }
}

// Export for use in other files (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        RecurringInvestment,
        RetirementWithdrawal,
        calculateRetirementJourney,
        CompoundingType,
        InvestmentType
    };
}
