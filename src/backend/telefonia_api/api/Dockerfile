# Use a Python image as the base
FROM python:3.9

# Update the system and install pkg-config and MySQL development files
RUN apt-get update && \
    apt-get install -y pkg-config default-libmysqlclient-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

# Copy the remainder of the files into the container
COPY . .

# Expose the port on which the Flask application will run
EXPOSE 80

# Command to start the Flask application
CMD ["python", "app.py"]