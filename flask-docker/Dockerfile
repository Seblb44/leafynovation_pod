# Use the official Python image as the base
FROM python:3.9-slim

# Set Git username variable for private repository
ENV GIT_USERNAME=Seblb44

# Set Git access token as an environment variable for private repository
ENV GIT_ACCESS_TOKEN=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

# Set the working directory in the container
WORKDIR /app

# Install git to clone the repo
RUN apt-get update && apt-get install -y git

# Clone your GitHub repository with the latest commit
RUN git clone https://${GIT_USERNAME}:${GIT_ACCESS_TOKEN}@github.com/Seblb44/Leafynovation_pod.git

# Change working directory to the flask-app folder inside the cloned repo
WORKDIR /app/Leafynovation_pod/flask-app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
