from turtle import title
from newsapi import NewsApiClient
from app import app
from flask import render_template




# api_key =app.config['MOVIE_API_KEY']

@app.route('/')
def getHeadline():
    newsapi =NewsApiClient(api_key='c9ec58711b3b40718d64f2d5c915c035')
    topheadlines =newsapi.get_top_headlines(country='us')

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    src =[]
    timePosted=[]

    for i in range(len(articles)):
        myarticles = articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        src.append(myarticles['url'])
        timePosted.append(myarticles['publishedAt'])


    mylist = zip(news, desc, img, src, timePosted)



    return render_template('base.html', title="Tophealines", context = mylist)



@app.route('/bbc')
def bbc():

    newsapi =NewsApiClient(api_key='c9ec58711b3b40718d64f2d5c915c035')
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    src =[]
    timePosted=[]


    for i in range(len(articles)):
        myarticles = articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        src.append(myarticles['url'])
        timePosted.append(myarticles['publishedAt'])


    mylist = zip(news, desc, img, src, timePosted)
    return render_template('bbc.html', title="bbc", context=mylist)


@app.route('/business')
def business():

    newsapi =NewsApiClient(api_key='c9ec58711b3b40718d64f2d5c915c035')
    topheadlines = newsapi.get_top_headlines(category='business')


    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    src =[]
    timePosted=[]


    for i in range(len(articles)):
        myarticles = articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        src.append(myarticles['url'])
        timePosted.append(myarticles['publishedAt'])


    mylist = zip(news, desc, img, src, timePosted)
    return render_template('bbc.html', title="bbc", context=mylist)
