# ⚽ La Liga Results Scraper (Selenium + Excel)

This project is a Python-based web scraper that uses **Selenium** to collect Spanish La Liga match results from a dynamic, JavaScript-rendered website.

## 📌 Summary

- ✅ **Rows Scraped:** 761 matches  
- 🕸️ **Website Type:** JavaScript-loaded (dynamic)  
- 📁 **Output Format:** Excel (XLSX)  
- 🧰 **Tools Used:** Python, Selenium, ChromeDriver, openpyxl

---

## ⚙️ Features

- 🖥️ Opens browser and navigates to La Liga section
- ⏳ Waits for full page and table data to load dynamically
- 📊 Extracts:
  - Team Names
  - Match Score
  - Match Date
- 📤 Saves clean results to `la_liga_results.xlsx`
- ✅ Output ready for performance analysis and historical tracking

---

## 🧰 Tech Stack

- Python 3.x  
- Selenium  
- ChromeDriver  
- openpyxl  
- time (for delay handling)

---

## ▶️ How to Run

1. **Install dependencies**
```bash
pip install selenium openpyxl
```


2.Download ChromeDriver
Make sure ChromeDriver is installed and added to your system PATH.

3.Run the script
```bash
python la_liga_scraper.py
```

4.Output
The file la_liga_results.xlsx will be created in your project folder.

📚 Use Cases
Match results analysis and visualization

Team performance tracking over time

Building football statistics dashboards

Data practice with dynamic websites

⚠️ Disclaimer
This project is for educational and personal use only.
Always respect website terms of use and robots.txt when scraping dynamic content.
Avoid sending excessive or repeated requests to avoid being blocked.

🤝 Author
Ali Ahmed
https://github.com/AlyAhmed22


