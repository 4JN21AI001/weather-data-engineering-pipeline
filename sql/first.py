import pandas as pd
import os

def extract(csv_path):
    print("📂 Current Working Directory:", os.getcwd())
    df = pd.read_csv(csv_path)
    print("✅ Data Extracted successfully!")
    return df

def transform(df):
    print("\n Starting Transformation")
    df = df.drop_duplicates()
    df = df.dropna()
    df.columns = df.columns.str.strip()

    df['rooms_per_households'] = df['total_rooms'] / df['households']
    df['bedrooms_per_room'] = df['population'] / df['total_rooms']
    df['populatiion_per_household'] = df['population'] / df['households']
    df['ocean_proximity'] = df['ocean_proximity'].str.lower().str.strip()
    print("Transformation completed successfully")
    return df

def load(df, output_path):
    print("\n Starting Load step...")
    df.to_csv(output_path, index = False)
    print(f"Data saved successfully to : {output_path}")
    

if __name__ == "__main__":
    csv_path = "housing.csv"
    output_path = "clean_housing.csv"

    df = extract(csv_path)
    df = transform(df)
    load(df, output_path)