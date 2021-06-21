from flask import jsonify, request, url_for, current_app
from .. import db
from ..models import SurveyResponse, QuestionResponse
from . import api


@api.route('/responses/<int:id>')
def get_response(id):
    ##TODO
    pass

@api.route('/surveys/<str:id>/responses/')
def get_survey_responses(id):
    ##TODO
    pass

@api.route('/surveys/<str:id>/responses', methods=['POST'])
def new_survey_response(id):
    ##TODO
    pass
