# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Set environment variable for Streamlit
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Run the Streamlit app
CMD ["streamlit", "run", "app/main.py"]