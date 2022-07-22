# config.py

import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or 'Put a verry, verry secret string here %^8294!'