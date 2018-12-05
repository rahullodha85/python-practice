FROM python:latest
#FROM ubuntu:latest
#RUN apt-get update -y
#RUN apt-get install -y python3-pip python3-dev build-essential
COPY ./app /flask-app/app/
COPY ./requirements.txt /flask-app/
COPY ./*.py /flask-app/
WORKDIR /flask-app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py", "dockerized"]
#CMD ["sleep", "infinity"]