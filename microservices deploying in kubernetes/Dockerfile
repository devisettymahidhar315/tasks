# Use the official Python image from the Docker Hub
FROM python:3.10

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory

# Install dependencies
# RUN pip install -r requirements.txt
RUN pip install Flask
RUN pip install Flask Flask-SQLAlchemy
# Copy the current directory contents into the container at /app
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
