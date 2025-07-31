# backend/retriever.py

import faiss
import numpy as np

def build_faiss_index(embeddings: list):
    """
    Builds and returns a FAISS index from the given list of embeddings.
    """
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))
    print(f"📦 FAISS index built with {index.ntotal} vectors.")
    return index

def search_index(index, query_embedding, top_k=3):
    """
    Searches the index and returns indices + distances of top_k matches.
    """
    distances, indices = index.search(np.array([query_embedding]).astype("float32"), top_k)
    return indices[0], distances[0]
