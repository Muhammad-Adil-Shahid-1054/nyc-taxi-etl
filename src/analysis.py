import duckdb

SILVER_PATH = "data/silver/yellow_tripdata_2019-01.parquet"

def analyze_data():
    conn = duckdb.connect()
    
    # ONE query to rule them all
    query = f"""
        SELECT 
            count(*) as total_trips,
            avg(trip_distance) as avg_distance,
            max(tip_amount) as max_tip
        FROM '{SILVER_PATH}'
    """
    
    print(f"Analyzing {SILVER_PATH}...")
    df_result = conn.execute(query).df()
    
    print(df_result)

if __name__ == "__main__":
    analyze_data()