
# Step 1: Turn your documents into embeddings (vectors), and store them

# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Our Q3 2026 sales were $2.4 million, up 15% from Q2.",
    "The engineering team shipped 12 new features in Q3.",
    "Customer satisfaction scores improved to 4.6/5 in Q3."
]

doc_embeddings = embedder.encode(documents)   # convert each document into a vector




# Step 2: Store these embeddings in a vector database


# pyrefly: ignore [missing-import]
import numpy as np
# pyrefly: ignore [missing-import]
import faiss   # a popular vector search library

dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

