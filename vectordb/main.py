import os
from pypdf import PdfReader

documents = []

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folder_path = os.path.join(BASE_DIR, "documents")

for file_name in os.listdir(folder_path):

    if file_name.endswith(".pdf"):

        file_path = os.path.join(folder_path, file_name)

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text

        documents.append({
            "file_name": file_name,
            "content": text
        })

print(documents)

def chunk_text(text, chunk_size=300):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(words[i:i + chunk_size])

        chunks.append(chunk)

    return chunks

all_chunks = []

for doc in documents:

    chunks = chunk_text(doc["content"])

    for chunk in chunks:

        all_chunks.append({
            "file_name": doc["file_name"],
            "chunk": chunk
        })

print(all_chunks)

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

chunk_texts = [item["chunk"] for item in all_chunks]

embeddings = model.encode(chunk_texts)

import chromadb

client = chromadb.Client()

collection = client.create_collection(name="career_docs")

for i, item in enumerate(all_chunks):

    collection.add(

        documents=[item["chunk"]],

        embeddings=[embeddings[i].tolist()],

        ids=[f"chunk_{i}"],

        metadatas=[{
            "source": item["file_name"]
        }]
    )

query = "who are the employees working in neftura renewables pvt ltd"

query_embedding = model.encode(query).tolist()

results = collection.query(

    query_embeddings=[query_embedding],

    n_results=4
)

retrieved_docs = results["documents"][0]

metadata = results["metadatas"][0]

distances = results["distances"][0]

print("\nTOP RETRIEVED RESULTS:\n")

for i in range(len(retrieved_docs)):

    print(f"Result {i+1}")

    print(f"Source File: {metadata[i]['source']}")

    print(f"Distance Score: {distances[i]}")

    print("\nChunk Content:\n")

    print(retrieved_docs[i])

    print("\n" + "-" * 80 + "\n")

import ollama


# -------------------------------
# COMBINE RETRIEVED CHUNKS
# -------------------------------

context = "\n".join(retrieved_docs)


# -------------------------------
# USER QUERY
# -------------------------------

user_question = "Who is the employee?"


# -------------------------------
# SEND TO OLLAMA
# -------------------------------

response = ollama.chat(

    model="llama3",

    messages=[

        {
            "role": "system",

            "content": """
            You are a helpful AI assistant.

            Answer ONLY from the provided context.

            Keep answers short and precise.

            If answer is not available in the context,
            say 'Answer not found in context.'
            """
        },

        {
            "role": "user",

            "content": f"""
            Context:
            {context}

            Question:
            {user_question}
            """
        }
    ]
)


# -------------------------------
# FINAL ANSWER
# -------------------------------

print("\nFINAL ANSWER:\n")

print(response["message"]["content"])

def retrieve_documents(query, n_results=4):

    query_embedding = model.encode(query).tolist()

    results = collection.query(

        query_embeddings=[query_embedding],

        n_results=n_results
    )

    return results