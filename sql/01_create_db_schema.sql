
-- Create Warehouse access
USE ROLE ACCOUNTADMIN;
USE WAREHOUSE compute_wh;

-- Create Database & Schema
CREATE OR REPLACE DATABASE weather_snow;
USE DATABASE weather_snow;

CREATE OR REPLACE SCHEMA curated;
USE SCHEMA curated;
