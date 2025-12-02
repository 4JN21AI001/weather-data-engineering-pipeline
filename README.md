Weather Data Engineering Pipeline (AWS + Snowflake)

A fully working end-to-end Data Engineering pipeline that extracts real-time weather data from a Public API, stores it in AWS Data Lake (S3), and loads curated data into Snowflake for analytics.

 Architecture Overview:
 
Weather API → Python Ingestion → S3 Raw Zone
                    ↓
              Python Transform
                    ↓
              S3 Processed Zone
                    ↓
              Snowflake Stage
                    ↓
          Curated Table for Analytics
                    ↓
          SQL Queries + BI Tools  


| Layer | Tools |
|------|------|
| Data Source | Weather API |
| Ingestion | Python (Requests, Boto3), Scheduling (future) |
| Data Lake | AWS S3 |
| Data Warehouse | Snowflake |
| Analytics | SQL Queries |
| Version Control | GitHub |

Project Structure:

python/
├── weather-ingest.py # API → S3 Raw Zone
├── weather-transform.py # Raw → Processed Zone
sql/
├── 01_create_db_schema.sql
├── 02_create_stage.sql
├── 03_create_load_table.sql


How to Run the Pipeline

1.Ingest Data from Weather API into S3: python3 python/weather-ingest.py

2.Transform Data (clean + CSV formatting): python3 python/weather-transform.py

3.Load Data into Snowflake and Execute SQL scripts in this order:
3.1_create_db_schema.sql
3.2_create_stage.sql
3.3_create_load_table.sql




## 👤 Author

**Abhishek Badiger**  
Aspiring Data Engineer | AI/ML Engineer  

🔗 LinkedIn: [https://www.linkedin.com/in/<your-profile>](https://www.linkedin.com/in/abhishek-badiger-460814339/)  
📦 GitHub: [https://github.com/4JN21AI001  ](https://github.com/4JN21AI001)


