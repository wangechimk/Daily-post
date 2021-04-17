from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sources/<name>')
def sources(name):
    return render_template("sources.html")