from sentence_transformers import SentenceTransformer
import os
import json

CHUNK_SIZE = 512
model = SentenceTransformer("intfloat/e5-small")

code_chunks = []

for root, _, files in os.walk("./data/codebase"):
    for file in files:
        if file.endswith(".tsx") or file.endswith(".ts") or file.endswith(".js"):
            with open(os.path.join(root, file), 'r') as f:
                code = f.read()
                for i in range(0, len(code), CHUNK_SIZE):
                    chunk = code[i:i+CHUNK_SIZE]
                    vec = model.encode(chunk)
                    code_chunks.append({"text": chunk, "embedding": vec.tolist()})

with open("./data/vector_store/chunks.json", "w") as out:
    json.dump(code_chunks, out) 