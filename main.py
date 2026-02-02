from src.ingest import download_file
from src.transform import transform_data            
from src.analysis import analyze_data 
import os

URL= 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-01.csv.gz'
BRONZE_DIR = "data/bronze/yellow_tripdata_2019-01.csv.gz"

def main():
    print("Starting NYC Taxi ETL Pipeline...")
    download_file(URL, BRONZE_DIR)
    print("Download step completed.")
    print("Starting data transformation step...")
    transform_data()
    print("Data transformation step completed.")
    print("Starting data analysis step...") 
    analyze_data()
    print("Data analysis step completed.")

if __name__ == "__main__":
    main()