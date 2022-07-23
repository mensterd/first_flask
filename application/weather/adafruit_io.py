# adafruit_io

from configparser import ConfigParser
from urllib.request import urlopen, Request
from urllib import error
import json, sys, os

CONFIG_FILE_NAME = 'secrets.ini'
basedir = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(basedir, CONFIG_FILE_NAME)

BASE_ADAFRUIT_IO_API_URL = 'https://io.adafruit.com/api/v2/'


def _get_api_key():
    """Fetch the API key from the configuration file.

    Expects a configuration file with structure:

    [adafruit_io]
    username=<YOUR-USERNAME>
    token=<YOUR-ACCESS-TOKEN>
    """

    config = ConfigParser()
    config.read(config_file)
    # return a tuple with username and token
    return (config['adafruit_io']['username'], config['adafruit_io']['token'])


def build_query_request(feed_key):
    """Build the URL for an API request to Adafruits IO platform.
    
    Args:
        feed_key (str): key of the Adafruit feed
        
    Returns:
        (str, {}): A tuple containing a URL formated String, and a Dictionary
        containg the acces token.
    """
    username, token = _get_api_key()
    query_headers = {'fx-aio-key': token}
    url = f'{BASE_ADAFRUIT_IO_API_URL}{username}/feeds/{feed_key}/data'
    return (url, query_headers)


def get_data(query_url, request_headers=None):
    """Get the data from the Adafruit feed.

    Args: query_url (str) fully formatted url to feed,
        request_headers (dict) containing the api-token info.

    Returns: last 100 records as JSON string


    """
    query_request = Request(query_url, headers=request_headers)
    try:
        with urlopen(query_request) as response:
            data = response.read()
            return json.loads(data)

    except error.HTTPError as e:
        if e.code == 401:  #Unauthorized
            sys.exit('Access denied, check your API key and username.')
        if e.code == 404:  # Not found
            sys.exit('Can\'t find data for this url.')
            # sys lets you exit the program without traceback
        else:
            sys.exit(f'Houston, we have a problem: ({e.code})')


def get_adafruit_io(feed_key):
    query_url, query_headers = build_query_request(feed_key)
    data = get_data(query_url, query_headers)
    return data


def main():
    data = get_adafruit_io('buitentemp')
    print(data)
    print('lenght: ', len(data))
    print(type(data))


if __name__ == '__main__':
    main()