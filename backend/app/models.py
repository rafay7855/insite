from typing import List

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


class Survey:
    def __init__(self, surveyid: int, category: str, questions: List):
        self.id = surveyid
        self.category = category
        self.questions = questions

    def to_json(self):
        questions = [q.to_json() for q in self.questions]
        json_survey = {
            'id': self.id,
            'category': self.category,
            'questions': questions
        }
        return json_survey


class Question:
    def __init__(self, number: int, text: str, response_type: str, alt_text=""):
        self.number = number
        self.response_type = response_type
        self.text = text
        self.alt_text = alt_text
    
    def to_json(self):
        json_question = {
            'number': self.number,
            'response_type' : self.response_type,
            'text': self.text,
            'alt_text': self.alt_text
        }
        return json_question
