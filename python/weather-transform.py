import boto3
import json
import pandas as pd
from io import BytesIO

BUCKET_NAME = "data-lake-weather-abhishek"

s3 = boto3.client('s3')

# List all raw weather files
response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="raw/weather/")
files = [item['Key'] for item in response.get('Contents', []) if item['Key'].endswith('.json')]

for file_key in files:
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=file_key)
    data = json.loads(obj['Body'].read().decode('utf-8'))

    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"],
        "humidity": data["hourly"]["relativehumidity_2m"],
        "wind_speed": data["hourly"]["wind_speed_10m"],
    })

    # Save to processed zone
    processed_key = file_key.replace("raw", "processed").replace(".json", ".csv")
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    
    s3.put_object(Bucket=BUCKET_NAME, Key=processed_key, Body=csv_buffer.getvalue())
    print(f"✅ Processed: s3://{BUCKET_NAME}/{processed_key}")
