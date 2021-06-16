from flask import jsonify, request, url_for, current_app
from .. import db
from tinydb import Query
#from ..models import Survey, Question
from . import api


@api.route('/surveys/')
def get_surveys():
    ##TODO
    pass

@api.route('/surveys/<identifier>')
def get_survey(identifier: str):
    Survey = Query()
    survey = db['surveys'].search(Survey.id == identifier)
    return survey

@api.route('/surveys/', methods=['POST'])
def new_survey():
    ##TODO
    pass

