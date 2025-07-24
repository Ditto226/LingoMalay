FROM python:3.10-slim
#FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime

# Install system packages like ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Set working directory inside container
WORKDIR /app

# Copy the requirements first to install dependencies
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app/ .

# Expose port for Uvicorn
EXPOSE 8080

# Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
