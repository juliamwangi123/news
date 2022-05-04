from app.config import DevConfig
from gettext import install
from flask import Flask, url_for
from requests import request

# initialize the app

app= Flask(__name__)
app.config['SECRET_KEY']='41932c548f4fdfa9f7c743348d71e732'
# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import requests


