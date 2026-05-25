import json

from rag_agent.main import ask_rag


with open("tests/golden_tests.json", "r") as f:

    tests = json.load(f)


for i, test in enumerate(tests):

    print("\n" + "=" * 80)

    print(f"TEST {i+1}")

    print("=" * 80)

    question = test["question"]

    print(f"\nQUESTION: {question}\n")

    result = ask_rag(question)

    print("\nRESULT:\n")

    print(result)