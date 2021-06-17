from flask import jsonify, request, url_for, current_app
from .. import db
from tinydb import Query
from ..models import Survey, Question
from . import api


@api.route('/surveys/')
def get_surveys():
    ##TODO - Pagination?
    pass

@api.route('/surveys/<identifier>')
def get_survey(identifier: str):
    s_query = Query()
    survey = db['surveys'].search(s_query.identifier == identifier)
    return survey

@api.route('/surveys/', methods=['POST'])
def new_survey():
    try:
        survey = Survey(request.json)
    except:
        # TODO:  handle invalid request
        pass
    db['surveys'].insert(survey.to_json())

