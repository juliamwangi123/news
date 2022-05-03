from app.config import DevConfig
from gettext import install
from flask import Flask, url_for
from requests import request

# initialize the app

app= Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import requests


