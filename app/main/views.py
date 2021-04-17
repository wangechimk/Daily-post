from app import app

@app.route('/')
def index():
    return "DailyPost2 Homepage"

@app.route('/sources')
def sources():
    return "Source articles"