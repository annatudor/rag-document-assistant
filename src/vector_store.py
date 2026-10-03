import chromadb
from src.config import CHROMA_PATH, COLLECTION_NAME

def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    return client.get_or_create_collection(name=COLLECTION_NAME)

def add_chunks(collection, chunks):
    ids = []
    embeddings = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(str(i))
        embeddings.append(chunk["embedding"])
        documents.append(chunk["text"])
        metadatas.append({"source": chunk["source"]})

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
    )

def search(collection, query_embedding, k):
    top_k_results = []
    results = collection.query(query_embeddings = query_embedding, n_results = k)

    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
      top_k_results.append({"text": doc, "source": meta["source"], "distance": dist})
    return top_k_results