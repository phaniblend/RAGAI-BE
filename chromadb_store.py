import chromadb
import json

client = chromadb.Client()
collection = client.get_or_create_collection(name="code_chunks")

with open("./data/vector_store/chunks.json") as f:
    chunks = json.load(f)

for i, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk["text"]],
        embeddings=[chunk["embedding"]],
        ids=[str(i)]
    ) 