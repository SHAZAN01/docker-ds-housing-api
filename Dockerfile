# Step 1: Choose a base image
# We're using 3.11-slim, which matches the libraries we installed.
FROM python:3.11-slim

# Step 2: Set a working directory
# This is where our code will live inside the container.
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Copy dependency file
# Copy *only* this file first to take advantage of Docker caching.
COPY requirements.txt .

# Step 4: Install dependencies
# Upgrade pip and install all packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Step 5: Copy project files
# Copy our 'app' folder (main.py, model.py)
COPY ./app /app/app
# Copy our 'model' folder (housing_model.pkl)
COPY ./model /app/model

# Step 6: Expose the port
# Tell Docker the container will listen on port 8000
EXPOSE 8000

# Step 7: Define the CMD
# The command to run when the container starts.
# This starts the Uvicorn server to run our FastAPI app.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]