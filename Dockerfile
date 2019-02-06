FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install flask
COPY . /app
WORKDIR /app/app
ENTRYPOINT ["python3"]
CMD ["demo.py"]