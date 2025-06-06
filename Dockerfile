# pull official base image
FROM python:3.12.4-slim-bookworm

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependency 
RUN apt-get update \
  && apt-get -y install gcc postgresql netcat-traditional \
  && apt-get clean \ 
  && apt-get -y install libpq-dev gcc \
  && pip install psycopg2
  
# install dependencies
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# change entrypoint to exe file 
COPY ./app/entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .


# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]