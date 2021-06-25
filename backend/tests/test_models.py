import unittest
from flask import current_app
from app import create_app
import app.models as models
import json

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        with open('/usr/src/insite/tests/data/sample.json') as file:
            self.test_data = json.load(file)

    def tearDown(self):
        self.app_context.pop()
    
    def test_question_constructor(self):       
        test_data = self.test_data[0]['questions'][0]
        question = models.Question(**test_data)
        self.assertDictContainsSubset(subset=test_data, dictionary=question.to_json())
    
    # def test_question_tojson(self):
    #     self.assertFalse(1)

    def test_survey_constructor(self):   
        test_data = self.test_data[0]
        survey = models.Survey(**test_data)
        
        self.assertDictContainsSubset(subset=test_data['questions'][0], dictionary=survey.questions[0].to_json())
        self.assertDictContainsSubset(subset=test_data['questions'][1], dictionary=survey.questions[1].to_json())
    # def test_survey_tojson(self):           
    #     self.assertFalse(1) 
    
    # def test_question_response_constructor(self):
    #     self.assertFalse(1)

    # def test_question_response_tojson(self):
    #     self.assertFalse(1) 

    # def test_survey_response_constructor(self):
    #     self.assertFalse(1) 

    # def test_survey_response_tojson(self):
    #     self.assertFalse(1) 
