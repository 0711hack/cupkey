FROM python:3.7

MAINTAINER Ben Lebherz "b@benleb.de"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev

# # We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]