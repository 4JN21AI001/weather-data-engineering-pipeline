import requests
import json
import boto3
import datetime

# Change this to your bucket name
BUCKET_NAME = "data-lake-weather-abhishek"   # <--- make sure it's correct

# Weather API (Bangalore)
url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&hourly=temperature_2m,relativehumidity_2m,wind_speed_10m"
response = requests.get(url).json()

# Create timestamped filename
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
file_key = f"raw/weather/weather_{timestamp}.json"

# Upload JSON to S3
s3 = boto3.client("s3")
s3.put_object(Bucket=BUCKET_NAME, Key=file_key, Body=json.dumps(response))

print(f"✅ Data uploaded to s3://{BUCKET_NAME}/{file_key}")
