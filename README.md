# European Commission Calls for Istanbul Bilgi University Researchers
A Python script to do automatic matchings of Istanbul Bilgi University researchers to the European Commission's Funding & Tenders Portal's call keywords concerning various research projects and proposals.

Calls scraping can be used for any project that needs to utilize Horizon calls for the 2021-2027 period. The rest of the code is specified for BİLGİ.


## 🌐 Funding Portal
[![EU Funding Portal](https://img.shields.io/badge/View-Funding_&_Tenders_Portal-blue?style=flat-square&logo=european-union)](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals?order=DESC&pageNumber=1&pageSize=50&sortBy=startDate&isExactMatch=true&status=31094501,31094502&programmePeriod=2021%20-%202027&frameworkProgramme=43108390)


**Deadline Colors:**
- <span style="color:red">🔴 Red</span> - Due in 10 days
- <span style="color:yellow">🟡 Yellow</span> - Due in 30 days
- <span style="color:green">🟢 Green</span> - All others


## Requirements  
![Python Version](https://img.shields.io/badge/Python-3.12.5-blue?logo=python)
![Libraries](https://img.shields.io/badge/Libraries-See_requirements.txt-orange)
  
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   
2. Start the main.exe file.

3. After the Excel files are compiled, flask will open the dashboard automatically.


⚠️ **WARNING**:
- "dash" might not be compatible with your current version. Try downgrading it to 1.2.0 or else. You can also remove the debug statement from the dashboard file.
- Python 3.12.5 will work best due to dependencies
