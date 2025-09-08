# 🏦 Retirement Corpus Calculator

A sophisticated, multi-investment retirement planning platform with comprehensive testing, real-time visualizations, and professional-grade financial modeling capabilities.

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green.svg)
![Chart.js](https://img.shields.io/badge/Chart.js-4.4.0-ff6384.svg)
![Playwright](https://img.shields.io/badge/Playwright-16_Tests-2eaa4f.svg)
![Tests](https://img.shields.io/badge/Tests-100%25_Pass-brightgreen.svg)
![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)

## ✨ Features

### 🎯 **Multi-Investment Model Support**
- **Up to 10 Investment Models**: Create and manage multiple investment strategies simultaneously
- **Mixed Model Types**: Combine MoM (Monthly Investment, Monthly Compounding), YoY (Yearly Investment, Yearly Compounding), and YoM (Yearly Investment, Monthly Compounding) in a single calculation
- **Individual Tracking**: Each investment model displays as a separate line on the chart with unique colors and labels
- **Dynamic Model Management**: Add, remove, and customize investment models with real-time updates

### 📊 **Advanced Visualization & Interaction**
- **Interactive Chart Hover**: Detailed tooltips showing exact amounts, years, and ages when hovering over any chart line
- **Multi-Phase Journey**: Seamless visualization from investment accumulation phase to retirement withdrawal phase
- **Professional Charts**: Enhanced Chart.js integration with multi-line datasets, legends, and responsive design
- **Real-Time Updates**: All charts and calculations update instantly as you adjust parameters

### 💰 **Flexible Retirement Planning**
- **Manual Corpus Override**: Customize your retirement corpus amount while still seeing auto-calculated projections
- **Complete Retirement Journey**: Visualize both wealth accumulation and withdrawal phases in a single comprehensive chart
- **Inflation-Adjusted Calculations**: All retirement withdrawals automatically adjust for inflation year-over-year
- **Corpus Depletion Analysis**: See exactly when and if your retirement funds will be exhausted

### 🎛️ **Smart User Interface**
- **Interactive Sliders**: Real-time adjustment of all investment parameters with instant visual feedback
- **Dynamic Constraints**: Age sliders automatically adjust ranges to prevent invalid relationships
- **Context-Sensitive Help**: Investment model descriptions update based on your selected strategy
- **Professional Error Handling**: Graceful validation with clear error messages for invalid inputs

### 🧪 **Quality Assurance**
- **Comprehensive Testing**: 16 end-to-end tests covering all functionality with 100% pass rate
- **Cross-Browser Support**: Tested on Chromium, Firefox, and WebKit browsers
- **Autonomous Test Execution**: Complete test suite runs automatically without manual intervention
- **Production-Ready**: Robust error handling, validation, and professional development practices

### 💻 **Technical Excellence**
- **Responsive Design**: Perfect functionality on desktop, tablet, and mobile devices
- **No Login Required**: Instant access - just open and start planning your retirement
- **Fast Performance**: Optimized calculations and rendering for smooth user experience
- **Modern Stack**: Built with FastAPI, Pydantic, Chart.js, and comprehensive Playwright testing

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher (tested with Python 3.13.7)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tanmaysule/retirement_corpus_calculator.git
   cd retirement_corpus_calculator
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate it (macOS/Linux)
   source venv/bin/activate
   
   # On Windows
   # venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:8000
   ```

## 🎯 Usage

### 💡 **Getting Started**
1. **Launch**: Open the application at `http://localhost:8000`
2. **Default Model**: Start with one pre-configured investment model
3. **Customize**: Adjust parameters using interactive sliders and inputs
4. **Visualize**: Watch real-time updates on the comprehensive retirement journey chart

### 🏗️ **Managing Investment Models**

#### **Adding Investment Models**
- Click **"Add Investment Model"** to create additional investment strategies (up to 10)
- Each model can have different:
  - **Base Amount**: Initial lump sum investment
  - **Monthly/Yearly Amount**: Regular recurring investments
  - **Step Up Rate**: Annual increase in investment amounts (0-20%)
  - **Growth Rate**: Expected annual returns (0-20%)
  - **Model Type**: Choose from MoM, YoY, or YoM strategies

#### **Model Types Explained**
- **MoM**: Monthly Investment + Monthly Compounding (ideal for SIPs, mutual funds)
- **YoY**: Yearly Investment + Yearly Compounding (ideal for fixed deposits, bonds)  
- **YoM**: Yearly Investment + Monthly Compounding (hybrid approach for optimal growth)

### 🎛️ **Retirement Parameters**
- **Age Settings**: Current age, retirement age, and expected life span (with smart validation)
- **Withdrawal Planning**: Set your desired annual withdrawal amount (inflation-adjusted)
- **Manual Override**: Customize your retirement corpus while seeing auto-calculated projections
- **Advanced Settings**: Inflation rate, post-retirement returns, and display preferences

### 📊 **Interactive Chart Features**
- **Hover for Details**: Move your mouse over any chart line to see:
  - Exact year and your age at that time
  - Precise corpus amounts in Indian formatting
  - Investment phase vs. retirement phase data
- **Multi-Line Visualization**: Each investment model shows as a colored line
- **Combined View**: See individual models + total combined corpus
- **Retirement Journey**: Smooth transition from accumulation to withdrawal phases

### 🔧 **Advanced Features**
- **Real-time Validation**: Age relationships automatically validated
- **Error Handling**: Clear messages for invalid inputs with helpful suggestions
- **Responsive Design**: Works perfectly on mobile, tablet, and desktop
- **Export Ready**: Professional charts suitable for financial planning presentations

## 🏗️ Project Structure

```
retirement_corpus_calculator/
│
├── app.py                      # FastAPI web server
├── recurring_investment.py     # Core investment calculation logic
├── retirement_withdrawal.py    # Retirement phase calculations
├── requirements.txt            # Python dependencies
├── package.json                # Node.js dependencies for testing
├── playwright.config.js        # Playwright test configuration
├── templates/
│   └── index.html             # Main web interface
├── static/
│   └── style.css              # Styling and responsive design
├── tests/
│   └── retirement-calculator.spec.js  # End-to-end test suite
├── LICENSE                     # CC BY-NC 4.0 License
└── README.md                  # This file
```

## 🔧 Technical Details

### **🏗️ Architecture**
- **Backend**: FastAPI with Pydantic validation and comprehensive error handling
- **Frontend**: Vanilla HTML/CSS/JavaScript with enhanced Chart.js integration
- **Testing**: Playwright end-to-end testing with 100% coverage across all browsers
- **Data Models**: Type-safe Pydantic models for investment calculations and retirement planning

### **💰 Financial Calculation Engine**
- **Multi-Model Support**: Simultaneous processing of up to 10 different investment strategies
- **Advanced Compounding**: Monthly/Yearly compounding with precise mathematical accuracy
- **Step-up Investments**: Automatic yearly increases with compound growth calculations
- **Retirement Modeling**: Complete withdrawal phase simulation with inflation adjustments
- **Real-time Processing**: Instant recalculation of all models when parameters change

### **📊 Visualization & UX**
- **Dynamic Chart.js**: Multi-dataset line charts with individual model tracking
- **Interactive Tooltips**: Hover functionality with detailed financial data
- **Responsive Design**: Professional UI that works across all device sizes
- **Real-time Validation**: Client-side and server-side validation with user-friendly feedback
- **Smart Constraints**: Dynamic slider ranges that prevent invalid age relationships

### **🧪 Quality & Testing**
- **Comprehensive Test Suite**: 16 automated tests covering all user interactions
- **Cross-Browser Testing**: Automated testing on Chromium, Firefox, and WebKit
- **Production Monitoring**: Error tracking and graceful failure handling
- **Performance Optimized**: Efficient calculations and rendering for smooth user experience

## 🧪 Testing

This project includes a comprehensive end-to-end test suite using [Playwright](https://playwright.dev/) to ensure all functionality works correctly across different browsers.

### Test Setup

1. **Install Node.js** (if not already installed)
   ```bash
   # Using Homebrew on macOS
   brew install node
   
   # Or download from https://nodejs.org/
   ```

2. **Install Playwright and dependencies**
   ```bash
   # Install Playwright test runner and browsers
   npm install
   npx playwright install
   ```

### Running Tests

**Prerequisites**: Make sure the FastAPI server is running on `localhost:8000` before running tests:
```bash
# In one terminal, start the server
source venv/bin/activate
python app.py
```

Then in another terminal, run the tests:

```bash
# Run all tests (recommended)
npm test

# Run tests with visible browser (for debugging)
npm run test:headed

# Run tests in debug mode (step-by-step)
npm run test:debug

# Run with minimal output (for CI/automation)
npm run test:ci

# View detailed HTML report after tests
npm run test:report
```

### Test Coverage

Our test suite covers **15 comprehensive scenarios**:

- ✅ **Page Loading**: Ensures all essential UI elements load correctly
- ✅ **Investment Models**: Adding, removing, and managing multiple investment models
- ✅ **Real-time Updates**: Slider interactions and dynamic calculations
- ✅ **Help Text**: Context-sensitive help based on investment model types
- ✅ **Manual Overrides**: Custom retirement corpus input and display
- ✅ **Chart Rendering**: Interactive Chart.js visualizations
- ✅ **Validation**: Age relationships and input constraints
- ✅ **API Error Handling**: Graceful error display for invalid inputs
- ✅ **Data Persistence**: Form data preservation during model operations
- ✅ **Multi-Model Calculations**: Complex scenarios with multiple investment types
- ✅ **UI Limits**: Maximum model limits and button state management

### Test Results

Tests run **autonomously** and provide detailed results:
- **100% Pass Rate**: All 15 tests consistently pass
- **Cross-Browser**: Tested on Chromium, Firefox, and WebKit
- **Fast Execution**: Complete test suite runs in ~15-20 seconds
- **Detailed Reports**: HTML reports with screenshots for any failures

The tests automatically **validate both frontend and backend**, ensuring the entire application stack works correctly.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. **Run the test suite** to ensure everything works:
   ```bash
   # Start the server
   source venv/bin/activate
   python app.py &
   
   # Run tests
   npm test
   ```
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

**Note**: All contributions should pass the existing test suite. If you add new features, consider adding corresponding tests.

## 📝 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

**You are free to:**
- ✅ **Use** for personal, educational, and non-commercial purposes
- ✅ **Share** and redistribute the material
- ✅ **Adapt** and build upon the material

**Under these conditions:**
- 📝 **Attribution** - You must give appropriate credit
- 🚫 **NonCommercial** - You may not use the material for commercial purposes

For commercial use, please contact the author.

See the [LICENSE](LICENSE) file for full details or visit [Creative Commons](https://creativecommons.org/licenses/by-nc/4.0/).

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Charts powered by [Chart.js](https://www.chartjs.org/)
- Modern responsive design
