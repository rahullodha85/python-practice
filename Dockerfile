FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install flask
COPY . /app
WORKDIR /app/app
ENTRYPOINT ["python"]
CMD ["demo.py"]