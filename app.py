from flask import Flask, request, jsonify
from retriever import retrieve_context
from model_runner import query_mixtral
import base64

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    query = request.json.get("query")
    obfuscated_prompt = request.json.get("obfuscated")
    context = retrieve_context(query)
    prompt = f"### Search Query:\n{query}\n\n### Obfuscated Prompt:\n{obfuscated_prompt}\n\n### Code Context:\n{context}\n\n### Answer:"
    result = query_mixtral(prompt)
    encoded = base64.b64encode(result.encode()).decode()
    return jsonify({"answer": encoded})

if __name__ == "__main__":
    app.run(debug=True) 