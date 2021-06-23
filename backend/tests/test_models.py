import unittest
from flask import current_app
from app import create_app

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_question_constructor(self):           
        self.assertFalse(1) 
    
    def test_question_tojson(self):
        self.assertFalse(1)

    def test_survey_constructor(self):           
        self.assertFalse(1) 
    
    def test_survey_tojson(self):           
        self.assertFalse(1) 
    
    def test_question_response_constructor(self):
        self.assertFalse(1)

    def test_question_response_tojson(self):
        self.assertFalse(1) 

    def test_survey_response_constructor(self):
        self.assertFalse(1) 

    def test_survey_response_tojson(self):
        self.assertFalse(1) 
