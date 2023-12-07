# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a volume named "servervol" and mount it at "/serverdata" in the container
VOLUME /serverdata

# Make port 12345 available to the world outside this container
# EXPOSE 12345

# Run server.py when the container launches
CMD ["python", "./server.py"]
