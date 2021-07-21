from flask import jsonify, request, url_for, current_app
from tinydb import Query
from .. import db
from ..models import Survey, Question
from . import api, errors

# Used primarily by frontend to get a list of available surveys
@api.route('/surveys/')
def get_surveys():
    # Getting all will work for now, but there should be better access.
    # Search by tags perhaps? Ask for certain fields?
    surveys = db['surveys'].all()
    if surveys:
        return jsonify({
            'surveys': [Survey(x).to_json() for x in surveys]
        })
    else:
        return errors.not_found()


# Used primarily by frontend to render a survey
@api.route('/surveys/<str:identifier>/')
def get_survey(identifier: str):
    s_query = Query()
    survey = db['surveys'].get(s_query['identifier'] == identifier)
    if survey:
        return jsonify(survey)
    else:
        return errors.not_found()


# Used manually to add a new survey.
# Since I'm making each of these for myself, I can just do it in JSON
# and send it with httpie or Postman or something.
# Fronted view for just sending JSON? could be convenient.
@api.route('/surveys/', methods=['POST'])
def new_survey():
    try:
        survey = Survey(**request.get_json())
        identifier = survey.identifier
    except:
        return errors.bad_request()
    db['surveys'].insert(survey.to_json())
    return jsonify(survey.to_json()), 201, \
        {'Location': url_for('api.get_survey', identifier=identifier)}

