import pandas as pd
import pytest
import os

SILVER_PATH = "data/silver/yellow_tripdata_2019-01.parquet"

def test_silver_file_exists():
    """Test to check if the silver Parquet file exists."""
    assert os.path.exists(SILVER_PATH), f"Silver file does not exist at {SILVER_PATH}"


def test_no_negative_trip_distance():
    df = pd.read_parquet(SILVER_PATH)
    negative_distances = df[df['trip_distance'] < 0]
    assert len(negative_distances) == 0

def test_column_exists():
    df = pd.read_parquet(SILVER_PATH)
    expected_columns = ['tpep_pickup_datetime', 'trip_distance', 'total_amount']
    for col in expected_columns:
        assert col in df.columns