# sensor_readings.py

from configparser import ConfigParser
from urllib import error, parse, request
import json
import sys

BASE_WEATHER_API_URL = 'https://weerlive.nl/api/json-data-10min.php'


def _get_api_key():
    """Fetch the API key from the configuration file.

    Expects a configuration file named 'secrets.ini' with structure:

    [weerlive]
    api_key=<YOUR-API-KEY>
    """

    config = ConfigParser()
    config.read('secrets.ini')
    # username en token in een dict stoppen?
    return config['weerlive']['api_key']


def build_weather_query(city_name):
    """Build the URL for an API request to Openweather's weather API.
    
    Args:
        city_input (list[str]): Name of a city as collected by argparse
        imperial (bool): Whether or not to use imperial units for temperature
        
    Returns:
        Str: URL formatted for a call to openWeather's city name endpoint
    """
    api_key = _get_api_key()
    url = f'{BASE_WEATHER_API_URL}?key={api_key}&locatie={city_name}'
    return url


def get_weather_data(query_url):
    """Makes an API request to a URL and returns the data as a Python object.

    Args:
        query_url (str): URL formatted for OpenWeather's city name endpoint

    Returns:
        dict: Weather information for a specific city
    """
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


def main():
    query = build_weather_query('waalre')
    print(query)
    result = get_weather_data(query)
    print(result)


if __name__ == '__main__':
    main()