from app.config import DevConfig
from gettext import install
from flask import Flask
from requests import request

# initialize the app

app= Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

from app import requests


