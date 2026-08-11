import os

os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_store(chunks):
    """
    Convert text chunks into embeddings and store them in FAISS.
    """

    if not chunks:
        raise ValueError("No text chunks found.")

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    ).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, chunks


def search_vector_store(index, chunks, query, top_k=3):
    """
    Search the most relevant chunks using semantic search.
    """

    if not chunks:
        return []

    # Never request more chunks than exist
    top_k = min(top_k, len(chunks))

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []
    seen = set()

    # Remove duplicate chunk indices
    for idx in indices[0]:

        if idx == -1:
            continue

        if idx in seen:
            continue

        seen.add(idx)

        results.append(chunks[idx])

    return results