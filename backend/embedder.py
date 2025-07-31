# backend/embedder.py

from sentence_transformers import SentenceTransformer

def get_embedder(model_name='all-MiniLM-L6-v2'):
    """
    Loads a sentence-transformer model for embeddings.
    Default: MiniLM - fast and accurate for short texts.
    """
    print(f"🔍 Loading embedding model: {model_name}")
    return SentenceTransformer(model_name)

def embed_chunks(embedder, chunks: list) -> list:
    """
    Embeds a list of text chunks using the loaded model.
    Returns a list of vector embeddings.
    """
    print(f"📏 Embedding {len(chunks)} chunks...")
    embeddings = embedder.encode(chunks, show_progress_bar=True)
    print("✅ Embedding complete.")
    return embeddings
