import os
from flask import Flask

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Add Config

from src import routes