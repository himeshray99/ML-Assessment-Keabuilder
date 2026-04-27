def build_prompt(context, query):
    return f"""
You are an AI assistant for a funnel-building platform.

Use ONLY the context below to answer.
If the answer is not in the context, say "I’m not sure".

Context:
{context}

Question:
{query}

Answer:
"""