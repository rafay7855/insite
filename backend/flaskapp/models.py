from typing import List

class SurveyResponse:
    def __init__(self, survey_id: int, responses: List):
        self.survey_id = survey_id
        self.responses = responses


class Survey:
    def __init__(self, surveyid: int, category: str, questions: List):
        self.id = surveyid
        self.category = category
        self.questions = questions
    

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
