from app import app
from .models import Sources, Articles
import urllib.request, json
from newsapi import NewsApiClient

key = app.config['API_KEY']
url = app.config['SOURCE_URL']
newsapi = NewsApiClient(api_key=key)


def sources():
    '''
    function that gets all english news sources in a list
    '''
    data = newsapi.get_sources(language='en',country='us', category='general')
    data_list = data['sources']
    source_list=[]
    for item in data_list:
        new_source = Sources(item['id'], item['name'], item['description'], item['url'])
        source_list.append(new_source)

    return source_list

    def articles(source_id):
    '''
    function that gets all english news sources in a list
    '''
    source_url = url.format(source_id, key)
    with urllib.request.urlopen(source_url) as uri:
        result = uri.read()
        response = json.loads(result)

        article_results = []

        if response['articles']:
            source_data_list = response['articles']
            article_results = get_data(source_data_list)
    return article_results


def get_data(source_dict):
    '''
    '''
    article_list = []
    for item in source_dict:
        title = item.get('title')
        author = item.get('author')
        description = item.get('description')
        url = item.get('url')
        url_to_image = item.get('urlToImage')
        published_at = item.get('publishedAt')

        if url_to_image and url:
            new_article = Articles(title, author, description, url, url_to_image, published_at)
            article_list.append(new_article)     
    return article_list 