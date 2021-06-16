from flask import jsonify, request, url_for, current_app
from .. import db
from ..models import Survey, Question
from . import api


@api.route('/surveys/')
def get_surveys():
    ##TODO
    pass

@api.route('/surveys/<int:id>')
def get_survey(id):
    ##TODO
    pass

@api.route('/surveys/', methods=['POST'])
def new_survey():
    ##TODO
    pass

