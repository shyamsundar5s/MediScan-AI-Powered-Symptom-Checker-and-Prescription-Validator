# Backend Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY ./backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./backend/app /app/app

# Expose the port and run the application
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
