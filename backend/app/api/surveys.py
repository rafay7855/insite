from flask import jsonify, request, url_for, current_app
from tinydb import Query
from .. import db
from ..models import Survey, Question
from . import api


@api.route('/surveys/')
def get_surveys():
    # req_json = request.get_json()
    # surveys_query = Query()
    surveys = db['surveys'].all()
    return jsonify({
        'surveys': [Survey(x).to_json() for x in surveys]
    })


@api.route('/surveys/<str:identifier>/')
def get_survey(identifier: str):
    s_query = Query()
    survey = db['surveys'].search(s_query['identifier'] == identifier)
    return jsonify(survey)


@api.route('/surveys/', methods=['POST'])
def new_survey():
    try:
        survey = Survey(**request.get_json())
        identifier = survey.identifier
    except:
        # TODO:  handle invalid request
        pass
    db['surveys'].insert(survey.to_json())
    return jsonify(survey.to_json()), 201, \
        {'Location': url_for('api.get_survey', identifier=survey.identifier)}

