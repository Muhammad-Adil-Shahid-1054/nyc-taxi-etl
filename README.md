# NYC Taxi Data Lakehouse (Local ETL)

## Project Overview
This project is a robust, local ETL (Extract, Transform, Load) pipeline that processes New York City Yellow Taxi trip data. It demonstrates a **Data Lakehouse architecture** by ingesting raw CSV data, enforcing schema constraints, converting to columnar Parquet format, and performing high-speed analytical queries using **DuckDB**.

**Key Metrics Processed:** ~7.6 Million Records
**Tech Stack:** Python, Pandas, DuckDB, Parquet, OS Module.

## 🏗 Architecture
The pipeline follows the **Medallion Architecture** pattern:

1.  **Bronze Layer (Raw):** - Ingests compressed CSV data (`.csv.gz`) from external sources.
    - Implements idempotent download logic to prevent redundant network requests.
2.  **Silver Layer (Cleansed):** - Loads raw data using Pandas.
    - Enforces strict data types (Datetime conversion).
    - Writes to **Parquet** format for 90% compression and faster columnar access.
3.  **Gold Layer (Analytics):** - Uses **DuckDB** for serverless SQL analysis.
    - Aggregates metrics (Total Trips, Avg Distance, Max Tip) in a single pass.

## 🔧 Setup & Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd nyc-taxi-etl

# Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt


#Run the project
python main.py
