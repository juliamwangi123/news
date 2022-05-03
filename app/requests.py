from turtle import title
from newsapi import NewsApiClient
from app import app
from flask import render_template




# api_key =app.config['MOVIE_API_KEY']

@app.route('/')
def getHeadline():
    newsapi =NewsApiClient(api_key='9415e0bb8a0b4215bbe997557e470d40')
    topheadlines =newsapi.get_top_headlines(country='us')

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    src =[]

    for i in range(len(articles)):
        myarticles = articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        src.append(myarticles['url'])


    mylist = zip(news, desc, img, src)



    return render_template('base.html', title="topNews", context = mylist)