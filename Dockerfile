# set base image (host OS)
FROM python:3.7-slim-buster

# set the working directory in the container
WORKDIR /src

# ENV http_proxy=http://proxy.mju.es:8080
# ENV https_proxy=http://proxy.mju.es:8080

# ENV no_proxy=localhost,127.0.0.1,.docker,.mju.es,.justicia.es

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
# Gunicorn script
#COPY run-gunicorn.sh .
#RUN chmod a+x run-gunicorn.sh
# Copy script to check health of container
#COPY healthcheck.sh .
#RUN chmod a+x healthcheck.sh

# command to run on container start
CMD [ "python", "-u", "app.py"]
#CMD ["python", "-um", "gunicorn", "-p", "gunicorn.pid", "--bind", "0.0.0.0:5003", "--workers", "2", "--log-level", "debug", "--capture-output", "--timeout", "600", "app:app" ]