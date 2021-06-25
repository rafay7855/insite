from flask import Flask
from flask_bootstrap import Bootstrap
from tinydb import TinyDB, database
import os
from config import configs

bootstrap = Bootstrap()

def create_app(configname):
    app = Flask(__name__)
    app.config.from_object(configs[configname])
    configs[configname].init_app(app)

    bootstrap.init_app(app) 
    # Using TinyDB until it becomes inadequate, then I will migrate to mongoDB
    # Requires using Docker bind mount to persist data. 
    # Will worry about that once I put this on my raspberry PI
    db_file = TinyDB('db.json')
    # Set up tables
    db = {
        'surveys': db_file.table('surveys'),
        'responses': db_file.table('responses')
    }
    
    @app.route('/')
    def hello():
        return '<h1>Hello World!</h1>'

    @app.route('/name/<name>')
    def user(name):
        return f'<h1>Hello {name}!</h1>'

    return app