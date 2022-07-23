# application/__init__.py


from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('_config.py')

from application.weather.views import weather_blueprint


# Register blueprints
app.register_blueprint(weather_blueprint)
