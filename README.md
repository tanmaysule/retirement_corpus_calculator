# 🏦 Retirement Corpus Calculator

<img width="1467" height="785" alt="image" src="https://github.com/user-attachments/assets/35f3f114-235a-4a7a-9300-c78b2e7e8acb" />
<img width="1422" height="803" alt="image" src="https://github.com/user-attachments/assets/30fdac9c-e24a-43d9-b134-2237e584eef5" />

A sophisticated, multi-investment retirement planning platform with comprehensive testing, real-time visualizations, and professional-grade financial modeling capabilities. **Now available as a live web application!**

🌐 **[Live Demo: https://tanmaysule.github.io/retirement_corpus_calculator/](https://tanmaysule.github.io/retirement_corpus_calculator/)**

![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg)
![Chart.js](https://img.shields.io/badge/Chart.js-4.4.0-ff6384.svg)
![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Live-brightgreen.svg)
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
- **Modern Stack**: Built with vanilla JavaScript, HTML5, Chart.js, and comprehensive Playwright testing

## 🚀 Quick Start

### 🌐 **Instant Access - No Installation Required!**

**Option 1: Use the Live Web Application**
1. **Visit the live site:** [https://tanmaysule.github.io/retirement_corpus_calculator/](https://tanmaysule.github.io/retirement_corpus_calculator/)
2. **Start planning:** All features work directly in your browser
3. **No setup needed:** Begin retirement planning immediately!

### 💻 **Local Development Setup**

**Prerequisites**
- Any modern web browser (Chrome, Firefox, Safari, Edge)
- Local web server (optional, for development)

**Option 2: Run Locally**

1. **Clone the repository**
   ```bash
   git clone https://github.com/tanmaysule/retirement_corpus_calculator.git
   cd retirement_corpus_calculator
   ```

2. **Serve the files** (choose one method):
   
   **Simple Python server:**
   ```bash
   python3 -m http.server 8000
   # Then open: http://localhost:8000
   ```
   
   **Node.js server:**
   ```bash
   npx serve .
   # Follow the provided URL
   ```
   
   **Or just open directly:**
   ```bash
   # Open index.html directly in your browser
   open index.html  # macOS
   # or double-click index.html in file explorer
   ```

## 🎯 Usage

### 💡 **Getting Started**
1. **Launch**: Visit [https://tanmaysule.github.io/retirement_corpus_calculator/](https://tanmaysule.github.io/retirement_corpus_calculator/) or run locally
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
├── index.html                  # Main web interface
├── js/
│   └── calculations.js         # Investment & retirement calculation engine
├── static/
│   └── style.css              # Styling and responsive design
├── package.json                # Node.js dependencies for testing
├── playwright.config.js        # Playwright test configuration
├── tests/
│   └── retirement-calculator.spec.js  # End-to-end test suite
├── LICENSE                     # CC BY-NC 4.0 License
└── README.md                  # This file
```

## 🔧 Technical Details

### **🏗️ Architecture**
- **Frontend**: Vanilla HTML/CSS/JavaScript with enhanced Chart.js integration
- **Calculations**: Pure JavaScript calculation engine with comprehensive financial modeling
- **Testing**: Playwright end-to-end testing with 100% coverage across all browsers
- **Deployment**: Static site hosted on GitHub Pages for instant global access

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
- **Real-time Validation**: Client-side validation with user-friendly feedback
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

**Prerequisites**: Make sure you have a local web server serving the application before running tests:

```bash
# Option 1: Simple Python server
python3 -m http.server 8000

# Option 2: Node.js server  
npx serve . --port 8000

# Option 3: Any other web server on port 8000
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

The tests automatically **validate the complete frontend application**, ensuring all calculations, interactions, and user interface elements work correctly across different browsers.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. **Run the test suite** to ensure everything works:
   ```bash
   # Start a local server (choose one)
   python3 -m http.server 8000 &
   # OR: npx serve . --port 8000 &
   
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

## 🚀 Deployment

This application is deployed as a static website on **GitHub Pages**, making it instantly accessible worldwide without any server requirements.

### **Live Site**
- **URL**: [https://tanmaysule.github.io/retirement_corpus_calculator/](https://tanmaysule.github.io/retirement_corpus_calculator/)
- **Hosting**: GitHub Pages (automatic deployment from main branch)
- **Performance**: Fast global CDN delivery
- **Uptime**: Backed by GitHub's infrastructure

### **Deploying Your Own Version**

1. **Fork this repository**
2. **Enable GitHub Pages**:
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / (root)
3. **Access your deployment**: `https://yourusername.github.io/retirement_corpus_calculator/`

The site will automatically update whenever you push changes to the main branch.

## 🙏 Acknowledgments

- Charts powered by [Chart.js](https://www.chartjs.org/)
- Testing framework: [Playwright](https://playwright.dev/)
- Hosted on [GitHub Pages](https://pages.github.com/)
- Modern responsive design with vanilla JavaScript
