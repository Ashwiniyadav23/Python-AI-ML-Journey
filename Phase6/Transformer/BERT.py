# pyrefly: ignore [missing-import]
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
results = classifier(["I love learning Python", "I hate spam"])
print(results)   # [{'label': 'POSITIVE', 'score': 0.99987}, {'label': 'NEGATIVE', 'score': 0.9997}]    


