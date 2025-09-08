# 🏦 Retirement Corpus Calculator

A beautiful, interactive web application to calculate and visualize retirement investment projections with real-time dynamic charts.

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green.svg)
![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)

## ✨ Features

- **Interactive Sliders**: Real-time adjustment of investment parameters
- **Dynamic Charts**: Beautiful Chart.js visualizations that update instantly
- **Investment Types**: Support for monthly/yearly investments and compounding
- **Step-up Investments**: Automatic yearly increases in investment amounts
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **No Login Required**: Simple, clean interface - just open and use!

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

1. **Adjust Parameters**: Use the interactive form to set:
   - Base Amount (₹)
   - Recurring Amount (₹) 
   - Step Up Rate (0-20%)
   - Average Growth Rate (0-20%)
   - Investment Start Year
   - Compounding Type (Monthly/Yearly)
   - Investment Type (Monthly/Yearly)
   - Years to Calculate (5-50 years)

2. **Real-time Updates**: The graph automatically updates as you change any parameter

3. **View Projections**: See your investment growth over time with precise year-by-year calculations

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

- **Backend**: FastAPI (modern, fast web framework)
- **Frontend**: Vanilla HTML/CSS/JavaScript with Chart.js
- **Calculations**: Custom investment calculation engine with support for:
  - Monthly/Yearly compounding
  - Step-up investments
  - Flexible investment schedules
  - Precise year-end calculations

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
