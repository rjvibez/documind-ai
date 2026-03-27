import faiss
import numpy as np

def create_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def search(index, query_vector, chunks, k=2):
    distances, indices = index.search(np.array([query_vector]), k)
    results = [chunks[i] for i in indices[0]]
    return results