from flask import Flask
from flask_bootstrap import Bootstrap
from tinydb import TinyDB
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

bootstrap = Bootstrap()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    bootstrap.init_app(app)
    db = TinyDB('db.json')
    
    from . import routes

    return app