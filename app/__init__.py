from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__,instance_relative_config=True)
app.config.from_object(DevelopmentConfig)
app.config.from_pyfile('config.py')

from app import views 