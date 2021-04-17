from app import app
from .models import Sources
from newsapi import NewsApiClient

key = app.config['API_KEY']
newsapi = NewsApiClient(api_key=key)


def sources():
    '''
    function that gets all english news sources in a list
    '''
    data = newsapi.get_sources(language='en',country='us')
    data_list = data['sources']
    source_list=[]
    for item in data_list:
        new_source = Sources(item['name'], item['description'], item['url'])
        source_list.append(new_source)

    return source_list