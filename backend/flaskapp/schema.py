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
    def __init__(self, text: str, responseType: str):
        self.text = text
        self.responseType = responseType 
