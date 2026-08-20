FROM python:3.12-slim

WORKDIR /app

# Install dependencies first so Docker can cache this layer between builds
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app ./app

# Azure App Service for Linux expects the container to listen on port 8000
# (or whatever WEBSITES_PORT is set to in App Service configuration)
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
