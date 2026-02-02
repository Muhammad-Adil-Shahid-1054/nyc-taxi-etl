import os 
import pandas as pd


INPUT_PATH = "data/bronze/yellow_tripdata_2019-01.csv.gz"
OUTPUT_PATH = "data/silver/yellow_tripdata_2019-01.parquet"

def transform_data():
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"Input file not found at {INPUT_PATH}")
    
    print(f"Reading data from {INPUT_PATH}...")
    df = pd.read_csv(INPUT_PATH, compression='gzip',  low_memory=False)
    print(f"Data read successfully. Number of records: {len(df)}")

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    print("Converted pickup and dropoff datetime columns to datetime objects.")

    df.to_parquet(OUTPUT_PATH, index=False, engine='pyarrow')
    print(f"Transformed data saved to {OUTPUT_PATH} in Parquet format.")

if __name__ == "__main__":
    transform_data()