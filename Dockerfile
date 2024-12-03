# Use a Python base image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Set environment variable to buffer stdout/stderr, useful in Docker
ENV PYTHONUNBUFFERED 1

# Set a working directory
WORKDIR /app

# Install system dependencies for building Python packages (e.g., pip)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt into the image
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app code into the container
COPY . /app/

# Expose port 8501 for Streamlit
EXPOSE 8501

# Set the entry point to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
