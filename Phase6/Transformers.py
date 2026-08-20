# Using Transformers — the Basic Pattern

# Example 1 — Using BERT for sentiment classification (no training needed, just using it)


# pyrefly: ignore [missing-import]
from transformers import pipeline


classifier = pipeline("sentiment-analysis")

result = classifier("I absolutely loved this movie!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9998}]


# Example 2 — Using GPT-2 for text generation


from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

result = generator("The future of AI is", max_length=30, num_return_sequences=1)
print(result[0]["generated_text"])
# "The future of AI is going to be shaped by how we choose to..."