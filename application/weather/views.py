# application/weather/views.py

from flask import Blueprint, render_template
from application.weather import adafruit_io as adafruit

# Create Blueprint object
weather_blueprint = Blueprint('weather', __name__)


@weather_blueprint.route('/')
@weather_blueprint.route('/home')
def index():
    return render_template('index.html')


@weather_blueprint.route('/weer')
def get_adafruit_weather():
    data = adafruit.get_adafruit_io('buitentemp')
    print(len(data))
    return (f'Op {data[0]["created_at"]} was het {data[0]["value"]}')
