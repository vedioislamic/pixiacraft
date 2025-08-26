# Base image
FROM python:3.10-slim

# Workdir
WORKDIR /app

# Install system dependencies (optional, Stable Diffusion ke liye zaroori hoti hain)
RUN apt-get update && apt-get install -y \
    git wget curl build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Make start.sh executable
RUN chmod +x start.sh

# Expose port (FastAPI default 8000)
EXPOSE 8000

# Start command
CMD ["./start.sh"]