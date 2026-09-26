def chunk_text(text, chunk_size, overlap):
    if overlap >= chunk_size:
            raise ValueError("The overlap cannot be greater or equal to chunk_size.")
    it = 0
    chunks = []
    while it < len(text):
        chunks.append(text[it:it+chunk_size])
        it += chunk_size - overlap
    return chunks

def chunk_documents(documents, chunk_size, overlap):
    chunked_docs = []
    for doc in documents: 
        chunks = chunk_text(doc["text"], chunk_size, overlap)
        for chunk in chunks:
           chunked_docs.append({"source": doc["source"], "text": chunk})
    return chunked_docs