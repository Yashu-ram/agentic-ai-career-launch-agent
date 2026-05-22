import sys
import os

# Add project root
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from ragas import evaluate

from ragas.metrics import (
    Faithfulness,
    ResponseRelevancy
)

from datasets import Dataset

from rag_agent.main import ask_question

from langchain_ollama import ChatOllama

from langchain_huggingface import HuggingFaceEmbeddings


# -----------------------------
# LOCAL OLLAMA MODEL
# -----------------------------
llm = ChatOllama(
    model="qwen2.5:3b"
)


# -----------------------------
# LOCAL EMBEDDINGS
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# QUESTIONS
# -----------------------------
questions = [

    "How well does this CV match this job description?",
]


answers = []
contexts = []
ground_truths = []


# -----------------------------
# RUN RAG PIPELINE
# -----------------------------
for question in questions:

    response = ask_question(question)

    answers.append(
      response["answer"]
)

    contexts.append(
      response["contexts"]
)

    ground_truths.append(
      response["ground_truth"]
)

    
# -----------------------------
# CREATE DATASET
# -----------------------------
dataset = Dataset.from_dict({
    "question": questions,
    "answer": answers,
    "contexts": contexts,
    "ground_truth": ground_truths
})


# -----------------------------
# RAGAS EVALUATION
# -----------------------------
rresult = evaluate(

    dataset=dataset,

    metrics=[
        Faithfulness(llm=llm),
        ResponseRelevancy(llm=llm)
    ],

    embeddings=embeddings,

    run_config={
        "timeout": 300
    }
)


# -----------------------------
# PRINT RESULTS
# -----------------------------
print("\n========== RAGAS SCORES ==========\n")
print(result)


# -----------------------------
# SAVE RESULTS
# -----------------------------
os.makedirs("evaluation", exist_ok=True)

with open(
    "evaluation/results.json",
    "w"
) as f:

    f.write(
        result.to_pandas().to_json(
            indent=2
        )
    )

print("\nResults saved to evaluation/results.json")