from turtle import title
from newsapi import NewsApiClient
from app import app
from flask import render_template


@app.route('/')
def getHeadline():
    return render_template('headlines.html', title="topNews")