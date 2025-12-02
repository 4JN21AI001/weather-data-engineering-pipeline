USE ROLE ACCOUNTADMIN;
USE WAREHOUSE compute_wh;
USE DATABASE weather_snow;
USE SCHEMA curated;

CREATE OR REPLACE STAGE weather_stage
URL='s3://data-lake-weather-abhishek/processed/weather/';
