USE DATABASE weather_snow;
USE SCHEMA curated;

-- Create table
CREATE OR REPLACE TABLE weather_hourly (
    time TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT
);

-- Load data from S3 Stage
COPY INTO weather_hourly
FROM @weather_stage
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1)
ON_ERROR = 'CONTINUE';
