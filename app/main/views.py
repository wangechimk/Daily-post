from . import main
from flask import render_template
from ..requests import sources, headlines, articles


@main.route('/')
def homepage():
    news_sources= sources()
    return render_template("index.html , news_sources=news_sources")

@main.route('/articles/<id>')
def all_articles(id):
    article_source = articles(id)
    print(article_source)
    return render_template("articles.html", article_source=article_source)