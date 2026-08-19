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