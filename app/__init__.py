from flask import Flask
from flask_monitor import Monitor
from flask_monitor.influxdb import ObserverInfluxdb

app = Flask(__name__)

monitor = Monitor('monitor', __name__)
app.register_blueprint(monitor)
monitor.add_observer(ObserverInfluxdb(host='127.0.0.1',
                                    port=8086,
                                    user='root',
                                    password='root',
                                    db='mydb'))

from app.demo import demo as demo

app.register_blueprint(demo)