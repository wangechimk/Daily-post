from app import app
from flask import render_template
from .requests import sources
import datetime as dt

@app.route('/')
def homepage():
    news_sources= sources()
    return render_template("index.html , news_sources=news_sources")

@app.route('/articles/<name>')
def articles(name):
    return render_template("articles.html")