import unittest
from flask import current_app
from app import create_app
import app.models as models
from typing import Dict
import json

# Tests are based around this particular data and its structure
sample_data_path = '/usr/src/insite/tests/data/sample.json'

class ModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        with open(sample_data_path) as file:
            self.test_data = json.load(file)

    def tearDown(self):
        self.app_context.pop()
    
   
    def test_question_constructor(self):       
        test_data = self.test_data[0]['questions'][0] # data-specific magic
        question = models.Question(**test_data)
        # Assert compare the given json with the generated json and confirm that
        # the data is represented correctly.
        self.assertDictContainsSubset(subset=test_data, dictionary=question.to_json())
    
 
    def test_survey_questions(self):   
        test_data: Dict = self.test_data[0]
        survey = models.Survey(**test_data)
        # Constructor creates questions correctly
        self.assertDictContainsSubset(subset=test_data['questions'][0], dictionary=survey.questions[0].to_json())
        self.assertDictContainsSubset(subset=test_data['questions'][1], dictionary=survey.questions[1].to_json())
        # Remove questions from our test data
        test_data.pop('questions')           
        # confirm everything else is correct
        self.assertDictContainsSubset(subset=test_data, dictionary=survey.to_json())
        
        

    
    # def test_question_response_tojson(self):
    #     self.assertFalse(1) 

    # def test_survey_response_constructor(self):
    #     self.assertFalse(1) 

    # def test_survey_response_tojson(self):
    #     self.assertFalse(1) 
