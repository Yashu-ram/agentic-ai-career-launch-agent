from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Sample sentences
sentences = [

    "Data analysts use SQL and Power BI",

    "Machine learning engineers build AI systems",

    "Doctors diagnose diseases in hospitals",

    "Python is widely used in data science",

    "Graphic designers create visual content"
]

# Create embeddings
embeddings = model.encode(sentences)

# Query
query = "AI and machine learning"

# Query embedding
query_embedding = model.encode(query)

# Cosine similarity
similarities = util.cos_sim(
    query_embedding,
    embeddings
)

# Extract scores
scores = similarities[0]

# Sort results
results = sorted(

    zip(sentences, scores),

    key=lambda x: x[1],

    reverse=True
)

# Create dataframe
df = pd.DataFrame([

    {
        "Sentence": sentence,
        "Similarity Score": round(float(score), 4)
    }

    for sentence, score in results
])

print("\nSemantic Search Results:\n")

print(df)