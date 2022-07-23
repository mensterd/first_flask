# application/weather/__init__.py

from flask import Flask
from application.weather.views import weather_blueprint

blueprint = Flask(__name__)
blueprint.register_blueprint(weather_blueprint)