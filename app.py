import streamlit as st
import requests
import numpy as np
from utils import load_docs, chunk_text
from rag.embed import get_embedding
from rag.prompt import build_prompt


# -----------------------------
# Cosine Similarity
# -----------------------------
def cosine_similarity(a, b):
    if a is None or b is None:
        return 0
    if len(a) == 0 or len(b) == 0:
        return 0
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# -----------------------------
# Retriever
# -----------------------------
class Retriever:
    def __init__(self, chunks):
        self.chunks = []
        self.embeddings = []

        for chunk in chunks:
            emb = get_embedding(chunk)

            if emb is not None and len(emb) > 0:
                self.chunks.append(chunk)
                self.embeddings.append(emb)

    def retrieve(self, query, top_k=2):
        query_emb = get_embedding(query)

        if query_emb is None:
            return []

        scores = [
            cosine_similarity(query_emb, emb)
            for emb in self.embeddings
        ]

        if not scores:
            return []

        top_idx = np.argsort(scores)[-top_k:][::-1]

        return [self.chunks[i] for i in top_idx]


# -----------------------------
# LLaMA (Ollama)
# -----------------------------
def generate(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data.get("response", "Error: No response from model.")

    except Exception as e:
        return f"Error: {str(e)}"


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="KeaBuilder AI", layout="centered")

st.title("KeaBuilder AI Chatbot (RAG + LLaMA)")
st.write("Ask questions about funnels, features, or the platform.")

# Load and prepare data
text = load_docs()
chunks = chunk_text(text)

# 🔥 Clean chunks (IMPORTANT)
chunks = [c.strip() for c in chunks if c.strip()]

# Build retriever
retriever = Retriever(chunks)

# Input
query = st.text_input("Enter your question:")

# Button
if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            context = retriever.retrieve(query)

            # 🔥 Handle empty context
            if not context:
                context = ["No relevant information found."]

            prompt = build_prompt(context, query)

            answer = generate(prompt)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Context")
        st.write(context)

    else:
        st.warning("Please enter a question.")