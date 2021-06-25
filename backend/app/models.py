from typing import List
import datetime as dt

# Defining the Data model
# Used to validate fields and types for db insertion
# These define the standard request format for the rest of the program

class SurveyResponse:
    """Represents a response to a survey.

    Attributes:
        survey_id: a string identifying the survey this question belongs to
        timestamp: an ISO formate datetime
        q_responses: a list of QuestionResponses to some or all of the questions in the survey
    """

    def __init__(self, **kwargs):
        self.survey_id = kwargs['survey_id']
        self.timestamp = dt.datetime.now().isoformat()
        self.q_responses = [QuestionResponse(**r) for r in kwargs['q_responses']]
    
    def to_json(self):
        question_responses = [r.to_json() for r in self.q_responses]
        json_survey_response = {
            'survey_id': self.survey_id,
            'q_responses': question_responses
        }
        return json_survey_response
    

class QuestionResponse:
    """Represents a response to a question

    Attributes:
        question_id: a string representing the ID of the question
        response: the response. type is the question's response type
    """
    def __init__(self, **kwargs):
        self.question_id = kwargs['question_id']
        self.response = kwargs['response']

    def to_json(self):
        json_question_response = {
            'question_id': self.question_id,
            'response': self.response
        }
        return json_question_response


class Question:
    """Represents a question in a survey.

    Attributes:
        survey_id: a string identifying the survey this question belongs to
        number: an integer denoting the number of this question.
        question_id: a unique identifier for this question based on number and survey_id
        response_type: a string denoting the type of response expected for this question
        text: the question itself.
        alt_text: optional alternative text
    """
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
        if self.alt_text:
            json_question['alt_text'] = self.alt_text
        return json_question


class Survey:
    """A survey containing questions.

    Attributes:
        identifier: a string identifying this survey. Used in other models as "survey_id"
        name: Human-readable name of the survey.
        tags: list of string tags for this survey
        response_type: a string denoting the type of response expected for this question
        text: the question itself.
        alt_text: optional alternative text
    """
    def __init__(self, **kwargs):
        self.identifier: str = kwargs['identifier']
        self.name: str = kwargs['name']
        self.created_at = dt.datetime.now().isoformat()
        self.tags: List[str] = kwargs['tags']
        self.questions: List = [Question(**q) for q in kwargs['questions']]
       

    def to_json(self):
        questions = [q.to_json() for q in self.questions]
        json_survey = {
            'identifier': self.identifier,
            'name': self.name,
            'tags': self.tags,
            'questions': questions
        }
        return json_survey

