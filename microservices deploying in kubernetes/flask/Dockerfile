# # Use the official Python image from the Docker Hub
# FROM python:3.10

# # # Set environment variables
# # ENV PYTHONDONTWRITEBYTECODE 1
# # ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the dependencies file to the working directory
# # COPY requirements.txt .

# # Install dependencies
# RUN pip install -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . .

# # Expose the port that Flask runs on
# EXPOSE 5000

# # Run the Flask application
# CMD ["python", "app.py"]

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install Flask

EXPOSE 5000


# Run the Flask application when the container launches
CMD ["python", "app.py"]
