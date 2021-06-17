from typing import List

# Defining the Data model
# Used to validate fields and types for db insertion
# These define the standard request format for the rest of the program

class SurveyResponse:
    def __init__(self, survey_id: int, q_responses: List, datetime):
        self.survey_id = survey_id
        self.q_responses = q_responses
        self.timestamp = 0
        ## TODO implement timestamp - ISO 8601?
    
    def to_json(self):
        question_responses = [r.to_json() for r in self.q_responses]
        json_survey_response = {
            'survey_id': self.survey_id,
            'q_responses': question_responses
        }
        return json_survey_response
    

class QuestionResponse:
    def __init__(self, number: int, response):
        self.number = number
        self.response = response

    def to_json(self):
        json_question_response = {
            'number': self.number,
            'response': self.response
        }
        return json_question_response


class Question:
    def __init__(self, **kwargs):
        self.survey_id = kwargs['survey_id']
        self.number: int = kwargs['number']
        # Generate question identifier
        self.question_id = f"{self.survey_id}-{self.number}"
        self.response_type: str = kwargs['response_type']
        # Questions may have alt text
        self.text: str = kwargs['text']
        if 'alt_text' in kwargs.keys():
            self.alt_text: str = kwargs['alt_text']
        else:
            self.alt_text: str = ''
    
    def to_json(self):
        json_question = {
            'survey_id': self.survey_id,
            'question_id': self.question_id,
            'number': self.number,
            'response_type' : self.response_type,
            'text': self.text,
        }
        if hasattr(self, 'alt_text'):
            json_question['alt_text'] = self.alt_text
        return json_question


class Survey:
    def __init__(self, **kwargs):
        self.identifier: str = kwargs['identifier']
        self.name: str = kwargs['name']
        self.category: str = kwargs['category']
        self.questions: List = [Question(q) for q in kwargs['questions']]

    def to_json(self):
        questions = [q.to_json() for q in self.questions]
        json_survey = {
            'identifier': self.identifier,
            'name': self.name,
            'category': self.category,
            'questions': questions
        }
        return json_survey

