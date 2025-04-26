# Use the official Python 3.8 base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask application port
EXPOSE 5000

# Define the command to start the Flask app
CMD ["python", "app.py"]
