from app import app
from flask import render_template
from .requests import sources,articles
import datetime as dt

@app.route('/')
def homepage():
    news_sources= sources()
    return render_template("index.html , news_sources=news_sources")

@app.route('/articles/<id>')
def all_articles(id):
    article_source = articles(id)
    print(article_source)
    return render_template("articles.html", article_source=article_source)