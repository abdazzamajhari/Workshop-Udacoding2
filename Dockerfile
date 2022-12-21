# Sets the base image for subsequent instructions
FROM python:3.10

# Sets the working directory in the container  
COPY . /app

# WORKDIR /app
WORKDIR /app

# Copies the dependency files to the working directory
# COPY requirements.txt /app/requirements.txt
# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copies everything to the working directory
# COPY . /app
# Command to run on container start    
ENTRYPOINT ["python3"]
CMD ["flask-api.py"]