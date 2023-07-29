# Do not modify the base image
FROM python:3.8-buster

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . /app/

# Install the required dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
