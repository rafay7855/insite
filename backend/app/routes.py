from flask import request, render_template
from flaskapp import app, db
from tindydb import Query


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello {name}!</h1>'
