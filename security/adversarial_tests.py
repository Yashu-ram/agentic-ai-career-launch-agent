from security.attack_prompts import (
    PROMPT_INJECTION,
    FAKE_CITATION,
    UNSAFE_AUTOMATION
)

from rag_agent.main import ask_rag


attacks = [

    ("PROMPT_INJECTION", PROMPT_INJECTION),

    ("FAKE_CITATION", FAKE_CITATION),

    ("UNSAFE_AUTOMATION", UNSAFE_AUTOMATION),
]


for name, attack in attacks:

    print("\n" + "=" * 80)

    print(f"RUNNING ATTACK: {name}")

    print("=" * 80)

    try:

        ask_rag(attack)

    except Exception as e:

        print(f"\nERROR: {e}\n")

    print("\nTEST COMPLETED")

    print("=" * 80)