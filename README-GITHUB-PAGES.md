# Retirement Corpus Calculator - GitHub Pages Setup

This repository contains a static version of the Retirement Corpus Calculator that can be hosted on GitHub Pages.

## 🚀 Live Demo

Once deployed, your calculator will be available at: `https://[your-username].github.io/retirement_corpus_calculator`

## 📁 File Structure (Static Version)

```
retirement_corpus_calculator/
├── index.html              # Main application file
├── static/
│   └── style.css           # Styling
├── js/
│   └── calculations.js     # JavaScript calculation logic
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions deployment
└── README-GITHUB-PAGES.md # This file
```

## 🛠️ Setup Instructions

### 1. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** tab
3. Scroll down to **Pages** section in the left sidebar
4. Under **Source**, select **GitHub Actions**
5. The workflow will automatically deploy your site on every push to main

### 2. Access Your Calculator

After the first deployment (which happens automatically when you push to main), your calculator will be available at:
`https://[your-username].github.io/retirement_corpus_calculator`

### 3. Custom Domain (Optional)

If you want to use a custom domain:
1. Add a `CNAME` file to your repository root with your domain name
2. Configure your DNS settings to point to GitHub Pages
3. Enable HTTPS in repository settings

## ✨ Features

- **Multi-Investment Model Support**: Create multiple investment strategies
- **Real-time Calculations**: All calculations happen in your browser
- **Interactive Charts**: Visualize your retirement journey
- **Responsive Design**: Works on desktop and mobile
- **No Backend Required**: Pure client-side application

## 🔧 Local Development

To test locally:

```bash
# Start a simple HTTP server
python3 -m http.server 8080
# Or use Node.js
npx serve .
# Or use any other static file server
```

Then open `http://localhost:8080` in your browser.

## 📊 How It Works

The calculator uses JavaScript to:
1. **Investment Phase**: Calculate compound growth using different models (Monthly/Yearly investing and compounding)
2. **Retirement Phase**: Simulate withdrawals with inflation adjustment
3. **Visualization**: Display the complete retirement journey on interactive charts

### Investment Models:
- **MoM**: Monthly investment with monthly compounding
- **YoY**: Yearly investment with yearly compounding  
- **YoM**: Yearly investment with monthly compounding

## 🚫 What Was Removed

The following Python backend components are no longer needed:
- `app.py` (FastAPI server)
- `requirements.txt` (Python dependencies)
- `recurring_investment.py` (converted to JavaScript)
- `retirement_withdrawal.py` (converted to JavaScript)
- `templates/` directory (no longer using Jinja2)
- Python virtual environment files

## 🐛 Troubleshooting

**Chart not loading?**
- Check browser console for JavaScript errors
- Ensure you're serving the files over HTTP (not file://)
- Verify Chart.js CDN is accessible

**Calculations not working?**
- Check that `js/calculations.js` is loaded properly
- Verify browser JavaScript is enabled
- Check for any console errors

## 🔄 Deployment

The site automatically deploys when you:
1. Push changes to the `main` branch
2. Create a pull request to `main`

The GitHub Actions workflow will:
1. Build the site
2. Deploy to GitHub Pages
3. Make it available at your GitHub Pages URL

## 📝 License

This project maintains the same license as the original repository.
