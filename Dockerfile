# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY fetch_top_models.py .

# Install required packages
RUN pip install requests

# Run the Python script
CMD ["python", "fetch_top_models.py"]
