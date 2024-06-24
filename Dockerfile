# Use an official Python runtime as a parent image
FROM python:3.9-slim

# RUN mkdir /user
# RUN mkdir /user/src
RUN mkdir  /app

# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-glx \
#     libglib2.0-0

# Set the working directory in the container to /app
WORKDIR /app


COPY requirements.txt .
# Add the current directory contents into the container at /app
ADD . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install deepface library
# RUN pip install --upgrade deepface

# Install tensorflow library
# RUN pip install tensorflow==2.9.0

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--reload"]
# CMD ["run.sh"]