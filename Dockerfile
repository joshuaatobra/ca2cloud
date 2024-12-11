# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /frontend

# Copy the current directory contents into the container
COPY . /frontend

# Install Flask
RUN pip install --no-cache-dir -r conditions.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Set the environment variable to run Flask in production
ENV FLASK_APP=frontend.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
