from sentence_transformers import SentenceTransformer

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(chunks):
    return model.encode(chunks)

def embed_query(query):
    return model.encode([query])[0]