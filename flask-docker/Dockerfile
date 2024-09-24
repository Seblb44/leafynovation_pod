# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install git to clone the repo
RUN apt-get update && apt-get install -y git

# Clone your GitHub repository with the latest commit
RUN git clone https://github.com/Seblb44/Leafynovation_pod.git /tmp/Leafynovation_pod

# Copy the flask-app folder from the cloned repo to the working directory
COPY /tmp/Leafynovation_pod/flask-app /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r /app/flask-app/requirements.txt

# Copy all files from the repository to the container
COPY /app/flask-app /app

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
