# ML-Assessment-Keabuilder
This project demonstrates a lightweight, production-oriented ML system designed for integration into the KeaBuilder platform.

📌 Overview

This project demonstrates a lightweight, production-oriented ML system designed for integration into the KeaBuilder platform.
It implements a Retrieval-Augmented Generation (RAG) pipeline using a locally hosted LLaMA model via Ollama. The system generates contextual and grounded responses based on structured platform data.
________________________________________
🚀 Features

•	Context-aware chatbot for KeaBuilder-related queries

•	Retrieval-Augmented Generation (RAG) pipeline

•	Local LLaMA inference using Ollama (no external APIs)

•	Embedding-based retrieval using cosine similarity

•	Simple and deployable Streamlit interface

🧠 System Architecture
User → Retriever → Context → LLaMA (Ollama) → Response
________________________________________
⚙️ How It Works

1. User enters a query in the Streamlit app
	
2. Query is converted into embeddings
	
3. Similarity is computed against stored document chunks
	
4. Top relevant chunks are retrieved
	
5. Context is injected into the prompt
	
6. LLaMA generates a grounded response
________________________________________
📸 Demo

<img width="940" height="492" alt="image" src="https://github.com/user-attachments/assets/28619feb-b5ea-4af1-a0db-2709fdce044f" />


<img width="940" height="605" alt="image" src="https://github.com/user-attachments/assets/a0faabde-123d-4a35-87a3-41879ba7d573" />

________________________________________

📂 Project Structure
Ml-assessment-Keabuilder/
│
├── app.py
├── utils.py
│
├── rag/
│   ├── embed.py
│   ├── retrieve.py
│   └── prompt.py
│
├── data/
│   └── docs.txt
└── requirements.txt
________________________________________
🛠️ Setup Instructions
1. Clone the repository
   git clone  <link>
   
2. cd ML-Assessment-Keabuilder

3. Create virtual environment
python -m venv venv
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Start Ollama
ollama serve

6. Run the app
streamlit run app.py
________________________________________
🧪 Sample Outputs

Q: What is KeaBuilder?

A: KeaBuilder is an AI-powered platform designed to help users build high-converting sales funnels, capture leads, and automate marketing workflows.

Q: Do you offer free trial?

A: KeaBuilder offers a 14-day free trial.

🧠 Data Note

The system uses structured sample data to simulate KeaBuilder platform knowledge.

In a production setup, this would be replaced with dynamic data sources such as databases or knowledge bases.
________________________________________
⚖️ Trade-offs

•	No vector database (used in-memory embeddings for simplicity)

•	Lightweight implementation for fast deployment

•	Local inference may be slower than hosted APIs
________________________________________
🚀 Future Improvements

•	Add vector database (e.g., Pinecone, FAISS)

•	Add chat history / memory

•	Improve UI/UX

•	Integrate real-time data sources
________________________________________
🎯 Key Design Decisions

•	Focused on simplicity and deployability

•	Used local LLaMA via Ollama to avoid API dependencies

•	Implemented RAG to reduce hallucination and improve response accuracy
________________________________________
🛠️ Tech Stack

•	Language: Python

•	UI: Streamlit

•	LLM Runtime: Ollama (LLaMA 3)

•	Embeddings: nomic-embed-text

•	Libraries: NumPy, requests
________________________________________________________________________________
✅ Summary
This project demonstrates a practical ML system that integrates retrieval and generation to provide reliable, context-aware responses, suitable for real-world SaaS platforms like KeaBuilder.



