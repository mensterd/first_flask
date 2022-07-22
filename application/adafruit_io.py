def get_temp_oud():
    X_AIO_KEY = 'code'
    UN = 'un'

    request_headers = {'fx-aio-key': X_AIO_KEY}

    url = f'https://io.adafruit.com/api/v2/{UN}/feeds/buitentemp/data'
   
    
    
    with urlopen(url) as response:
        body = response.read()


    data = json.dumps(body, indent=4)
    return data





def get_temp():
    X_AIO_KEY = 'aio_mvYP47ThBGYZdE3gpRePTxa5jPxb'
    UN = 'menster'

    request_headers = {'fx-aio-key': X_AIO_KEY}

    url = f'https://io.adafruit.com/api/v2/{UN}/feeds/buitentemp/data'
    parameters = {'limit': 1}


    response = requests.get(url, headers=request_headers, params=parameters)
    data = response.json()
    result = f"Temperatuur: {data[0]['value']} op: {data[0]['created_at']}"
    return result