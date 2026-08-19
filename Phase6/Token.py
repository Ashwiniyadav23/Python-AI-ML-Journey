# 1. Tokenization — breaking text into pieces a model can handle

text = "I love learning Python"
tokens = text.split()
print(tokens)   # ['I', 'love', 'learning', 'Python']


# 2. Embeddings — turning tokens into meaningful number vectors
# pyrefly: ignore [missing-import]
from gensim.models import Word2Vec

sentences = [["the", "cat", "sat", "on", "the", "mat"],
             ["the", "dog", "sat", "on", "the", "rug"]]

model = Word2Vec(sentences, vector_size=50, window=2, min_count=1)
print(model.wv["cat"])              # the embedding vector for "cat"
print(model.wv.most_similar("cat")) # words with the closest vectors


# 3. Attention — letting a model focus on the most relevant words


import numpy as np

def simple_attention(query, keys, values):
    scores = np.dot(keys, query)
    weights = np.exp(scores) / np.sum(np.exp(scores))
    output = np.dot(weights, values)
    return output, weights
keys = np.array([[1, 0], [0, 1], [1, 1], [0.5, 0.5]])   # "The", "trophy", "suitcase", "because"
values = keys.copy()
query = np.array([0.9, 0.9])   # roughly represents "it", "looking for" something like [1,1]

output, weights = simple_attention(query, keys, values)
print("Attention weights:", weights)
