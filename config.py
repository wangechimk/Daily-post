class Config:
    """
    """
    SOURCE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'  


class ProductionConfig(Config):
    """
    """
    pass


class DevelopmentConfig(Config):
    """
    """
    DEBUG = True 