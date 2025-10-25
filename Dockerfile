# Dockerfile 
FROM python:3.9-slim

# Set working directory
WORKDIR /app
# Copy requirements file to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . .
# Expose the port the app runs on
EXPOSE 5000
#run the application  
CMD [ "python","app.py" ]