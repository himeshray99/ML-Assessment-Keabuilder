import numpy as np
from rag.embed import get_embedding

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

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

        scores = [
            cosine_similarity(query_emb, emb)
            for emb in self.embeddings
        ]

        top_idx = np.argsort(scores)[-top_k:][::-1]
        return [self.chunks[i] for i in top_idx]