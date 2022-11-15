# set base image (host OS)
FROM python:3.7-slim-buster

# set the working directory in the container
WORKDIR /src

# Update libaries
RUN apt update -y && apt upgrade -y

# Install libaries
RUN apt install -y libaio1
RUN apt-get install -y libmagic1

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "-u", "app.py"]
