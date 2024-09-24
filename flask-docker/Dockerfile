# Set the working directory in the container
WORKDIR /app

# Install git to clone the repo
RUN apt-get update && apt-get install -y git

# Clone your GitHub repository with the latest commit
RUN git clone https://github.com/Seblb44/Leafynovation_pod.git /app \
    && cd /app/flask-docker/flask-docker \
    && git checkout 703099b9d293497d3895104dfe5c1c5059eba790

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r /app/flask-docker/flask-docker/requirements.txt

# Copy all files from the repository to the container
COPY /app/flask-docker/flask-docker /app

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
