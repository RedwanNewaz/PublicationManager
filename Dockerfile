# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to decode file
ENTRYPOINT ["python", "main.py"]