from flask import jsonify, request, url_for, current_app
from tinydb import Query
from .. import db
from ..models import SurveyResponse, QuestionResponse
from . import api, errors

@api.route('/surveys/<str:survey_id>/responses/')
def get_survey_responses(survey_id):
    resp = Query()
    responses = db['responses'].search(resp.survey_id == survey_id)
    if responses:
        return jsonify({
            'survey_responses': [SurveyResponse(r).to_json() for r in responses]
        })
    else:
        return errors.not_found()


@api.route('/surveys/<str:survey_id>/responses', methods=['POST'])
def new_survey_response(survey_id):
    try:
        survey_response = SurveyResponse(**request.get_json())
    except:
        return errors.bad_request() # returns
    db['responses'].insert(survey_response.to_json())
    return jsonify(survey_response.to_json()), 201
