import ollama
from src.config import SYSTEM_PROMPT
from src.config import GENERATION_MODEL
from src.embeddings import get_embedding
from src.vector_store import search

def build_prompt(question, chunks):
    labeled_chunks = []
    for i, chunk in enumerate(chunks):
        label = f"[Source {i+1}: {chunk['source']}]\n{chunk['text']}"
        labeled_chunks.append(label)
    context = "\n\n".join(labeled_chunks)

    user_prompt = f"Context:\n{context}\n\nQuestion: {question}"
    
    messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_prompt},
    ]
    return messages

def call_llm(messages):
    response = ollama.chat(
    model= GENERATION_MODEL,
    messages= messages,
    think=False,
    options={"temperature": 0},
)
    return response.message.content

def answear_question(question, collection, k = 3):
    sources = []
    query_question = get_embedding(question)
    chunks = search(collection, query_question, k)
    messages = build_prompt(question, chunks)
    answear = call_llm(messages)
    for chunk in chunks:
        sources.append(chunk["source"])
    return answear, sources 