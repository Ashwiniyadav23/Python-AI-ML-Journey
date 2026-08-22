from sentence_transformers import SentenceTransformer
import chromadb

# -------------------------
# STEP 1: Embedding Model
# -------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# -------------------------
# STEP 2: Documents
# -------------------------

sentences = [
    "Students must maintain 75% attendance.",
    "The minimum passing marks are 40%.",
    "Students can apply for leave through the student portal.",
    "The final examination is conducted at the end of the semester."
]


# -------------------------
# STEP 3: Create Embeddings
# -------------------------

embeddings = model.encode(sentences)


# -------------------------
# STEP 4: Create Vector DB
# -------------------------

client = chromadb.PersistentClient(path="./chroma_db")


# -------------------------
# STEP 5: Create Collection
# -------------------------

collection = client.get_or_create_collection(
    name="college_documents"
)


# -------------------------
# STEP 6: Store Data
# -------------------------

collection.add(
    ids=["1", "2", "3", "4"],
    documents=sentences,
    embeddings=embeddings.tolist()
)

print("Data stored successfully!")


# -------------------------
# STEP 7: User Question
# -------------------------

question = "How much attendance do I need?"


# -------------------------
# STEP 8: Convert Question
# -------------------------

question_embedding = model.encode(question)


# -------------------------
# STEP 9: Search Vector DB
# -------------------------

results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=2
)


# -------------------------
# STEP 10: Print Results
# -------------------------

print(results["documents"])