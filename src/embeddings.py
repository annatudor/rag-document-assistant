import ollama

def embed_chunks(chunks):
    embedded_vector = []
    for chunk in chunks: 
        response = ollama.embeddings(model="nomic-embed-text", prompt = chunk["text"])
        embedded_vector.append({"source": chunk["source"], "text": chunk["text"], "embedding": response["embedding"]})
    return embedded_vector 


