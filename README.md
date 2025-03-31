# 🔍 European Funding Matcher for Istanbul Bilgi University

A Python script to automatically match Istanbul Bilgi University researchers to the European Commission's Funding & Tenders Portal call keywords.

![Color-coded deadlines](https://img.shields.io/badge/Deadlines-Red%2C%20Yellow%2C%20Green-brightgreen)

## 🌐 Funding Portal
[![EU Funding Portal](https://img.shields.io/badge/View-Funding_&_Tenders_Portal-blue?style=flat-square&logo=european-union)](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?order=DESC&pageNumber=1&pageSize=50&sortBy=startDate&isExactMatch=true&status=31094501,31094502&programmePeriod=2021%20-%202027&frameworkProgramme=43108390)

**Deadline Colors:**
- <span style="color:red">🔴 Red</span> - Due in 10 days
- <span style="color:yellow">🟡 Yellow</span> - Due in 30 days
- <span style="color:green">🟢 Green</span> - All others

## 🛠 Requirements  
![Python Version](https://img.shields.io/badge/Python-3.12.5-blue?logo=python)
![Libraries](https://img.shields.io/badge/Libraries-See_requirements.txt-orange)
  
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   
2. Start the main.exe file.

3. After the Excel files are compiled, flask will open the dashboard automatically.

⚠️ **WARNING**:
- "dash" might not be compatible with your current version. Try downgrading it to 1.2.0 or else.
- Python 3.12.5 will work best due to dependencies
