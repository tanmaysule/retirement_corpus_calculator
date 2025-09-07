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
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html             # Main web interface
├── static/
│   └── style.css              # Styling and responsive design
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

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Activate virtual environment and test
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

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
