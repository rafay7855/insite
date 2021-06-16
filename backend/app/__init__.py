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
    db_file = TinyDB('db.json')
    db = {
        'surveys': db_file.table['surveys'],
        'responses': db_file.table['responses']
    }
    
    @app.route('/')
    def hello():
        return '<h1>Hello World!</h1>'

    @app.route('/user/<name>')
    def user(name):
        return f'<h1>Hello {name}!</h1>'

    return app