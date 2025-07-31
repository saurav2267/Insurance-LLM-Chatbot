# 🛡️ Insurance LLM Chatbot

An intelligent, LLM-powered chatbot built for **insurance business analysts**.  
It can understand and answer complex questions about CSV datasets like insurance claims — and even generate **charts** on demand.

---

## 🚀 Features

- ✅ **Ask Anything**: Query the dataset like a human (e.g. *"What is the average claim amount in Ohio?"*)
- 🧠 **LLM-Powered**: Uses Mistral via Ollama for fast, smart answers
- 🔎 **Semantic Search**: FAISS + embeddings for fast and relevant context retrieval
- 📊 **Chart Support**: Auto-generates bar charts from user queries (e.g. *"Show total claim amount by incident type"*)
- 💬 **Streamlit UI**: Simple, interactive chatbot frontend
- 👋 **Friendly Replies**: Handles casual greetings like "hi", "thank you", etc.

---

## 📂 Example Questions

> “What’s the most common type of car accident?”  
> “Plot total claim amount by incident city”  
> “How many claims reported fraud in Columbus?”  
> “Hi” → "Hello! 👋 I'm your insurance assistant."

---

## 🧱 Tech Stack

| Component | Tool |
|----------|------|
| Language Model | `Mistral` via [Ollama](https://ollama.com/) (Free, Local) |
| Embeddings | `all-MiniLM-L6-v2` via `sentence-transformers` |
| Vector Search | `FAISS` |
| Frontend | `Streamlit` |
| Charts | `Matplotlib` |
| Language | Python 3.10 |
| Dataset | Sample: `insurance_claims.csv` (40 columns, 1000 rows)

---

## ⚙️ How to Run Locally

> Prerequisites:
- Python 3.10+
- Git
- Ollama installed and running (`ollama run mistral`)

```bash
# Clone the repo
git clone https://github.com/your-username/insurance-llm-chatbot.git
cd insurance-llm-chatbot

# Set up virtual environment
python -m venv venv
.\venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the chatbot UI
streamlit run ui/interface.py
```
---

## 📊 Dataset Credit

This project uses a public dataset available from Kaggle:

**Auto Insurance Claims Dataset**  
🔗 [Kaggle - Auto Insurance Claims](https://www.kaggle.com/datasets/buntyshah/auto-insurance-claims-data) 

All rights belong to the original dataset author.

---
