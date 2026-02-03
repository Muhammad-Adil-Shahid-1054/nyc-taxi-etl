# 1. Base Image: Start with a lightweight Linux version that has Python 3.9 installed
FROM python:3.9-slim

# 2. Setup: Create a folder named 'app' inside the container
WORKDIR /app

# 3. Caching: Copy requirements.txt FIRST
# Docker is smart. If this file hasn't changed, it skips re-installing libraries.
COPY requirements.txt .

# 4. Install: Download the libraries (Pandas, DuckDB, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Code: Move your source code (src folder and main.py) into the container
COPY . .

# 6. Run: The command to execute when the container starts
CMD ["python", "main.py"]