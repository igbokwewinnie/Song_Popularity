FROM python:3.10

# Ensure stdout/stderr logs appear in real-time
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy code and models
COPY app/ /app/app/
COPY src/ /app/src/
COPY models/ /app/models/

# Install dependencies
COPY app/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
