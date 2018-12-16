import sys

from flask import Flask
from flask_monitor import Monitor
from flask_monitor.influxdb import ObserverInfluxdb
from app.helpers.configloader import ConfigLoader

app = Flask(__name__)

config_loader = ConfigLoader()
if (sys.argv.__len__()>1):
    env = sys.argv[1]
    app.config.update(config_loader.load(env))
else:
    app.config.update(config_loader.load())

monitor = Monitor('monitor', __name__)
app.register_blueprint(monitor)
monitor.add_observer(ObserverInfluxdb(host=app.config.get('influx_db_host'),
                                    port=app.config.get('influx_db_port'),
                                    user='root',
                                    password='root',
                                    db='mydb'))

from app.demo import demo as demo

app.register_blueprint(demo)