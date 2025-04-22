# Use the official Python 
FROM python:3.12.10-slim-bullseye

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application code into the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run
CMD ["python", "main.py"]