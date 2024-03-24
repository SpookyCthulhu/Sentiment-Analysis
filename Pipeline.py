from transformers import pipeline
sentiment_pipeline = pipeline('sentiment-analysis')
data = ['''Nobody in the AI trenches like us 

We have the biggest bubble in the history of bubbles with AI — I really think everyone is severely underestimating how much money is going to be injected into AI 

TRILLIONS ON TRILLIONS 

Don’t fuck this life changing opportunity up''']
print(sentiment_pipeline(data))