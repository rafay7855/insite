from flask import request, render_template
from flaskapp import app, db
from tindydb import Query


@app.route('/')
def index():
    return render_template("index.html")




