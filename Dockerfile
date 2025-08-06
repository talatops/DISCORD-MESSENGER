# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all source code
COPY . .

# Set environment variables (optionally for production)
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "main.py"]
