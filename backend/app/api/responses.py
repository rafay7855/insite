from flask import jsonify, request, url_for, current_app
from tinydb import Query
from .. import db
from ..models import SurveyResponse, QuestionResponse
from . import api, errors

@api.route('/surveys/<str:survey_id>/responses/')
def get_survey_responses(survey_id):
    # Query DB for responses to this survey
    resp = Query()
    responses = db['responses'].search(resp.survey_id == survey_id)
    # TODO: Add deeper querying of responses. Return last x responses
    if responses:
        # TODO Add Pagination
        return jsonify({
            'responses': [SurveyResponse(r).to_json() for r in responses]
        })
    else: # Apparently its code 204 when the multi-get is  empty
        return jsonify({'responses': []}), 204


# Used by the front-end (and others eventually) to log new data
@api.route('/surveys/<str:survey_id>/responses', methods=['POST'])
def new_survey_response(survey_id):
    try:
        # Current validation is only checking types using the model object
        survey_response = SurveyResponse(**request.get_json())
    except:
        return errors.bad_request() 
    # Insert this response into DB
    db['responses'].insert(survey_response.to_json())
    return jsonify(survey_response.to_json()), 201 



# TODO: add 