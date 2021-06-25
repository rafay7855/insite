from flask import jsonify
from . import api
from app.exceptions import ValidationError

def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status = 400
    return response

def not_found():
    response = jsonify({'error': 'not found'})
    response.status = 404
    return response
