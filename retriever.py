import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/e5-small")
client = chromadb.Client()
collection = client.get_collection(name="code_chunks")

def retrieve_context(query):
    qvec = model.encode(query).tolist()
    results = collection.query(query_embeddings=[qvec], n_results=5)
    return "\n\n".join(results["documents"][0]) 