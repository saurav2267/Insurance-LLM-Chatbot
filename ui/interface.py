# ui/interface.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from backend.csv_loader import load_csv, dataframe_to_chunks
from backend.embedder import get_embedder, embed_chunks
from backend.retriever import build_faiss_index, search_index
from backend.plotter import generate_chart
from llm.local_llm import generate_response

st.set_page_config(page_title="Insurance LLM Chatbot", layout="centered")
st.title("🛡️ Insurance Chatbot (LLM-Powered)")
st.markdown("Ask questions about your insurance claims dataset")

# Load and cache
@st.cache_resource(show_spinner=False)
def prepare_chatbot(file_path="data/insurance_claims.csv"):
    df = load_csv(file_path)
    chunks = dataframe_to_chunks(df)
    embedder = get_embedder()
    embeddings = embed_chunks(embedder, chunks)
    index = build_faiss_index(embeddings)
    return df, chunks, embedder, index

df, chunks, embedder, index = prepare_chatbot()

# Chat section
user_query = st.text_input("💬 Enter your question:")

if user_query:
    # 🔹 Basic Chit-Chat Handler
    friendly_greetings = {
        "hi": "Hello! 👋 I'm your insurance assistant. Ask me anything about your dataset.",
        "hello": "Hi there! 😊 How can I help you with your insurance data?",
        "hey": "Hey! I'm here to answer any questions about the claims.",
        "thanks": "You're welcome! Let me know if you need anything else.",
        "thank you": "Happy to help! 😊",
        "how are you": "I'm just a bot, but I'm functioning at 100%! 😄 Ask me anything."
    }

    lowered = user_query.lower().strip()
    if lowered in friendly_greetings:
        st.markdown("### 🤖 Answer:")
        st.write(friendly_greetings[lowered])
        st.stop()

    # 🔹 Detect chart-related query
    if any(word in lowered for word in ["chart", "plot", "visualize", "graph"]):
        result = generate_chart(user_query, df)
        if result:
            st.warning(result)
    else:
        with st.spinner("Thinking..."):
            query_vec = embedder.encode([user_query])[0]
            top_ids, _ = search_index(index, query_vec)
            context = "\n".join([chunks[i] for i in top_ids])
            answer = generate_response(context, user_query)

        st.markdown("### 🤖 Answer:")
        st.write(answer)

        with st.expander("🔍 View context used by LLM"):
            for i in top_ids:
                st.write(f"- {chunks[i]}")
