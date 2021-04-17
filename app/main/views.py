from app import app
from flask import render_template
from .requests import sources,articles
import datetime as dt

@app.route('/')
def homepage():
    news_sources= sources()
    return render_template("index.html , news_sources=news_sources")

@app.route('/articles')
def articles():
    source_articles = articles()
    return render_template("articles.html", source_articles=source_articles)