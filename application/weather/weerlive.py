from configparser import ConfigParser
from urllib import error, parse, request
import json
import sys


class Weerlive:

    BASE_WEATHER_API_URL = 'https://weerlive.nl/api/json-data-10min.php'

    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.api_config_file_name = 'secrets.ini'


    def __repr__(self):
        return f'Het weer voor {self.city}'

    def _read_api_key_from_file():
        config = ConfigParser()
        config.read(self.api_config_file_name)
        return config['weerlive']['api_key']


    def _build_weather_query(self):        
        url = f'{self.BASE_WEATHER_API_URL}?key={self.api_key}&locatie={self.city}'
        return url

    def get_weather_data(self):
        query_url = self._build_weather_query()

        try:
            response = request.urlopen(query_url)
        except error.HTTPError as http_error:
            if http_error.code == 401:  #Unauthorized
                sys.exit('Access denied, check your API key.')
            if http_error.code == 404:  # Not found
                sys.exit('Can\'t find weather data for this city.')
                # sys lets you exit the program without traceback
            else:
                sys.exit(f'Houston, we have a problem: ({http_error.code})')

        data = response.read()

        try:
            return json.loads(data)
        except json.JSONDecodeError:
            sys.exit('Couldn\t read the server response.')