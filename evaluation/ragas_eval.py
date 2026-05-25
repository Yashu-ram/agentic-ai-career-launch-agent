import sys
import os

# =========================================================
# ADD PROJECT ROOT
# =========================================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# =========================================================
# IMPORTS
# =========================================================

from datasets import Dataset

from rag_agent.main import ask_rag

from langchain_ollama import ChatOllama

from langchain_huggingface import HuggingFaceEmbeddings


# =========================================================
# LOCAL OLLAMA MODEL
# =========================================================

llm = ChatOllama(
    model="qwen2.5:3b"
)


# =========================================================
# LOCAL EMBEDDINGS
# =========================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================================================
# QUESTIONS
# =========================================================

questions = [

    "How well does this CV match this job description?"
]


# =========================================================
# STORE RESULTS
# =========================================================

answers = []

contexts = []

ground_truths = []


# =========================================================
# RUN RAG PIPELINE
# =========================================================

for question in questions:

    response = ask_rag(question)

    # Skip failed responses
    if response is None:
        continue

    # ==============================================
    # ANSWERS
    # ==============================================

    answers.append(
        response.answer
    )

    # ==============================================
    # CONTEXTS
    # ==============================================

    contexts.append([
        " ".join(response.citations)
    ])

    # ==============================================
    # HUMAN GROUND TRUTH
    # ==============================================

    ground_truths.append(
        "The resume matches SQL and Power BI skills but lacks Kubernetes and cloud computing experience."
    )


# =========================================================
# CREATE DATASET
# =========================================================

dataset = Dataset.from_dict({

    "question": questions,

    "answer": answers,

    "contexts": contexts,

    "ground_truth": ground_truths
})


# =========================================================
# MANUAL EVALUATION
# =========================================================

print("\n========== MANUAL EVALUATION ==========\n")

for i in range(len(questions)):

    print(f"\nQUESTION:\n{questions[i]}\n")

    print(f"GENERATED ANSWER:\n{answers[i]}\n")

    print(f"GROUND TRUTH:\n{ground_truths[i]}\n")

    print(f"RETRIEVED CONTEXT:\n{contexts[i]}\n")

    print("=" * 60)


# =========================================================
# SAVE RESULTS
# =========================================================

os.makedirs(
    "evaluation",
    exist_ok=True
)

results_data = {

    "question": questions,

    "answer": answers,

    "ground_truth": ground_truths,

    "contexts": contexts
}

import json

with open(
    "evaluation/results.json",
    "w"
) as f:

    json.dump(
        results_data,
        f,
        indent=2
    )

print("\nResults saved to evaluation/results.json")