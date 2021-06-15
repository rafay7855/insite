import os
from flask import Flask
from tinydb import TinyDB

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db = TinyDB('db.json')

# Add Config
from flaskapp import routes
