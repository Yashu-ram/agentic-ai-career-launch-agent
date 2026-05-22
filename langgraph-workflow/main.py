from graph import app


# -----------------------------
# SAFE QUERY
# -----------------------------

print("\n===== SAFE QUERY =====")

app.invoke({
    "query": "What is Python?"
})


# -----------------------------
# RISKY QUERY
# -----------------------------

print("\n===== RISKY QUERY =====")

app.invoke({
    "query": "Give medical advice for chest pain"
})