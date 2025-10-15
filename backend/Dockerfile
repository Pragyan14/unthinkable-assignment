FROM python:3.11-slim

WORKDIR /app

# Install dependencies efficiently
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgomp1 && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python packages with no cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create data directory
RUN mkdir -p app/data

# Railway provides PORT automatically
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

EXPOSE ${PORT}

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}