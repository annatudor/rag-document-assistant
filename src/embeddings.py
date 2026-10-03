import ollama
from src.config import EMBEDDING_MODEL

def embed_chunks(chunks):
    embedded_vector = []
    for chunk in chunks: 
        response = ollama.embeddings(model = EMBEDDING_MODEL, prompt = chunk["text"])
        embedded_vector.append({"source": chunk["source"], "text": chunk["text"], "embedding": response["embedding"]})
    return embedded_vector 

def get_embedding(text):
    response = ollama.embeddings(model=EMBEDDING_MODEL, prompt=text)
    return response["embedding"]