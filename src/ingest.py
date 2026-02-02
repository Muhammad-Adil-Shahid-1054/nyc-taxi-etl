import os
import requests
import gzip
import shutil

# 1. Configuration - Always avoid hardcoding paths deep in your logic
# We are using Jan 2019 data (approx 130MB compressed)
DOWNLOAD_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-01.csv.gz"
LOCAL_FILENAME = "yellow_tripdata_2019-01.csv.gz"
BRONZE_DIR = "data/bronze"
OUTPUT_PATH = os.path.join(BRONZE_DIR, LOCAL_FILENAME)

def download_file(url, output_path):
    """
    Downloads a file from a URL to a local path.
    Uses streaming to handle large files without eating up RAM.
    """
    # Check if directory exists, if not, create it
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Idempotency Check: Don't download if it already exists
    if os.path.exists(output_path):
        print(f"File already exists at {output_path}. Skipping download.")
        return

    print(f"Downloading {url}...")
    
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status() # Stop if the link is broken (404/500)
            
            # Write the file in chunks (standard practice for big data)
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        print(f"Download complete: {output_path}")

    except Exception as e:
        print(f"Error downloading file: {e}")
        # Clean up partial files so we don't have corrupted data later
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == "__main__":
    download_file(DOWNLOAD_URL, OUTPUT_PATH)