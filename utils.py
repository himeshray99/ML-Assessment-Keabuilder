import os


def load_docs(file_path="data/docs.txt"):
    """
    Load text data from a file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        raise ValueError("Document is empty")

    return text


def chunk_text(text, chunk_size=150):
    """
    Split text into meaningful chunks using sentence boundaries.
    """
    sentences = text.split(".")
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        # Add sentence if it fits
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    # Add last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def preview_chunks(chunks, n=3):
    """
    Utility function to preview first few chunks (for debugging).
    """
    return chunks[:n]