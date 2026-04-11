📌 Automated Weather Data Pipeline (API → BigQuery)
📖 Overview

This project is an automated ETL pipeline that collects weather data from public APIs, processes it using Python, and loads it into Google BigQuery for analysis.

The pipeline is designed to run automatically and deliver clean, structured data with minimal manual effort.

⚙️ What This Project Does
Extracts weather data from API
Cleans and transforms raw JSON data
Stores structured data in BigQuery
Logs execution and handles errors
Can run automatically on a schedule
🏗 Architecture

Data Sources:

Weather API (Open-Meteo)
Geolocation API (IP-based)

Processing:

Python (data cleaning and transformation with Pandas)

Storage:

Google BigQuery (data warehouse)
CSV (local backup/logs)

Automation:

Bash script
Cron scheduling
🚀 Key Features
Automated pipeline – runs without manual intervention
Error handling & retries – stable execution even if API fails
Environment configuration – secure storage of credentials using .env
Logging system – track execution and debug issues
Fallback logic – handles API failures gracefully
🧰 Tech Stack
Technology	Purpose
Python	Core logic
Pandas	Data transformation
Requests	API integration
Google BigQuery	Data storage
Bash / Cron	Automation
📊 Data Preview

Example output:

city	temperature	humidity	timestamp
Kyiv	12°C	65%	2026-04-01
▶️ How to Run
Clone the repository
Install dependencies
Create .env file (see .env.example)
Add your API keys and credentials
Run:
bash run.sh
🔄 Automation

The pipeline can be scheduled using cron to run automatically (e.g. every hour or daily).

💡 Business Value

This solution can be adapted for:

automated data collection
marketing dashboards
analytics pipelines
real-time data monitoring
📚 Learning Outcomes
Built a full ETL pipeline from API to cloud storage
Worked with Google BigQuery (data warehouse)
Implemented automation and logging
Improved handling of real-world data issues
