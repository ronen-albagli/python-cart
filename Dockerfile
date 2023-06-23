# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .
COPY .env .


# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m venv venv

RUN source venv/bin/activate || echo "Virtual environment activation failed"


# Copy the entire application code to the container
COPY . .

# Expose the desired port for your Flask application (e.g., 5000)
EXPOSE 8004

# Define the command to run your Flask application
CMD ["python", "app.py"]