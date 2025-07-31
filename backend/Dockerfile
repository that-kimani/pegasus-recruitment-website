# Base Image
FROM python:3.13-alpine

# Set the workdir
WORKDIR /app

# # Install system dependencies
# RUN apk add --no-cache build-base libpq-dev postgresql-dev

# Copy and install requirements.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code.
COPY . .

# Expose port
EXPOSE 5000

# Start the server
CMD ["gunicorn", "--chdir", "/app", "root.wsgi:application", "--bind", "0.0.0.0:5000"]