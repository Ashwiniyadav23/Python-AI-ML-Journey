# Example 2 — Using GPT-2 for text generation


# pyrefly: ignore [missing-import]
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
result  = generator("The quick brown fox jumps over", max_length=50, num_return_sequences=1)
print(result)   # [{'generated_text': 'The quick brown fox jumps over the lazy dog. \n\n  This is a great story about a fox and a dog who live together.'}]   