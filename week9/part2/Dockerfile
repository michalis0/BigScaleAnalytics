FROM ubuntu:18.04

MAINTAINER Your Name "ajal.ahmad@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en

COPY . /app
EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "application.py" ]
