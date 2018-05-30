
from aylienapiclient import textapi


class TextSentiment():
    def __init__(self,app_id='',app_key=''):
        self.APP_KEY=app_key
        self.APP_ID=app_id
        self.client = textapi.Client(self.APP_ID, self.APP_KEY)
    
    def analyze(self,text):
        sentiment = self.client.Sentiment({'text': text})
        mood=sentiment['polarity']
        confidence=sentiment['polarity_confidence']
        return mood,confidence


