# app.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))  # Add project root to import path

from backend.csv_loader import load_csv, dataframe_to_chunks
from backend.embedder import get_embedder, embed_chunks
from backend.retriever import build_faiss_index, search_index
from llm.local_llm import generate_response

# === Step 1: Load and chunk CSV ===
df = load_csv("data/insurance_claims.csv")
chunks = dataframe_to_chunks(df)
print("✅ Loaded CSV with shape:", df.shape)
print("✅ Converted", len(chunks), "rows to text chunks.")
print("Sample chunk:\n", chunks[0])

# === Step 2: Embedding ===
embedder = get_embedder()
print("🔍 Loading embedding model...")
embeddings = embed_chunks(embedder, chunks)
print("✅ Embedding complete.")
print("🔢 First embedding vector (truncated):", embeddings[0][:5])

# === Step 3: Build FAISS Index ===
index = build_faiss_index(embeddings)

# === Step 4: Query Example ===
query = "Were there any major car collisions in Ohio?"
query_vec = embedder.encode([query])[0]
matched_ids, matched_dists = search_index(index, query_vec)

print("\n🔍 Query Results:")
for i, dist in zip(matched_ids, matched_dists):
    print(f"🔗 Match (Distance: {dist:.4f}):\n{chunks[i]}\n")

# === Step 5: Get Answer from LLM ===
relevant_chunks = [chunks[i] for i in matched_ids]
context = "\n".join(relevant_chunks)
answer = generate_response(context, query)

print("🧠 LLM Answer:\n", answer)
