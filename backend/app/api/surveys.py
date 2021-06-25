from flask import jsonify, request, url_for, current_app
from tinydb import Query
from .. import db
from ..models import Survey, Question
from . import api, errors


@api.route('/surveys/')
def get_surveys():
    # req_json = request.get_json()
    # surveys_query = Query()
    surveys = db['surveys'].all()
    if surveys:
        return jsonify({
            'surveys': [Survey(x).to_json() for x in surveys]
        })
    else:
        return errors.not_found()


@api.route('/surveys/<str:identifier>/')
def get_survey(identifier: str):
    s_query = Query()
    survey = db['surveys'].get(s_query['identifier'] == identifier)
    if survey:
        return jsonify(survey)
    else:
        return errors.not_found()


@api.route('/surveys/', methods=['POST'])
def new_survey():
    try:
        survey = Survey(**request.get_json())
        identifier = survey.identifier
    except:
        return errors.bad_request()
    db['surveys'].insert(survey.to_json())
    return jsonify(survey.to_json()), 201, \
        {'Location': url_for('api.get_survey', identifier=survey.identifier)}

