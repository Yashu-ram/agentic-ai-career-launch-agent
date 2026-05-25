# 🚀 Career Launch Agent

A production-grade AI-powered Career Launch Agent built using Retrieval-Augmented Generation (RAG), ChromaDB vector search, FastAPI, and local LLMs.

The system helps users analyze resumes against job descriptions, identify missing skills, generate improvement roadmaps, and provide structured AI-powered career guidance while implementing safety guardrails and evaluation pipelines.

---

# 🎯 Why This Project

Traditional AI chatbots may hallucinate, provide unsafe outputs, or generate unreliable career advice.

This project was built to explore:
- Secure AI system design
- Retrieval-Augmented Generation (RAG)
- Structured JSON outputs
- AI safety guardrails
- Prompt injection defense
- Evaluation and reliability testing

The goal was to create a safer and more reliable AI assistant for career guidance workflows.

---

# ✨ Features

- Resume and Job Description Analysis
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database Retrieval
- Embedding-based Semantic Search
- Structured JSON Outputs
- Pydantic Validation
- Retry Handling for Invalid Outputs
- Prompt Injection Detection
- Human Review Escalation
- Sensitive Topic Detection
- FastAPI Backend API
- Golden Test Evaluation Suite
- Output Validation & Normalization

---

# 🏗️ System Architecture

```text
User Query
    ↓
Safety Filters
    ↓
Retriever
    ↓
ChromaDB Vector Search
    ↓
Qwen2.5 via Ollama
    ↓
Structured JSON Output
    ↓
Pydantic Validation
    ↓
Output Guardrails
    ↓
FastAPI Response
```

---

# 📂 Project Structure

```text
career-launch-agent/
│
├── api/
│   └── app.py
│
├── rag_agent/
│   ├── main.py
│   ├── schema.py
│   └── rag_agent.ipynb
│
├── security/
│   ├── input_guard.py
│   ├── output_guard.py
│   ├── review_gate.py
│   └── topic_guard.py
│
├── tests/
│   └── golden_tests.json
│
├── evaluation/
│   └── run_tests.py
│
├── docs/
│   ├── system-card.md
│   └── failure-report.md
│
├── Documents/
│   ├── resumes/
│   └── job_descriptions/
│
├── embeddings/
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── uv.lock
```

---

# 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- ChromaDB
- SentenceTransformers
- Ollama
- Qwen2.5
- Pydantic
- Uvicorn
- Pytest
- uv

---

# 🛡️ Safety Features

- Prompt Injection Detection
- Sensitive Topic Detection
- Human Review Escalation
- Output Validation
- Structured Response Enforcement
- Retry Handling for Malformed JSON

---

# ✅ Evaluation & Reliability

The project includes:
- Golden test evaluation suite
- Structured schema validation
- Retry logic for malformed outputs
- Output normalization
- Failure documentation
- Safety guardrails

---

# 📊 Test Results

```bash
5/5 tests passed
```

Test coverage includes:
- Prompt injection detection
- Citation validation
- Structured response schema
- Human review escalation
- Empty query handling

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Yashu-ram/agentic-ai-career-launch-agent.git
cd agentic-ai-career-launch-agent
```

---

## Create Virtual Environment

```bash
uv venv
```

---

## Activate Virtual Environment

### Windows PowerShell

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv sync
```

---

# 🤖 Install Ollama

Download and install Ollama:

https://ollama.com/download

---

# 📥 Pull Qwen Model

```bash
ollama pull qwen2.5:3b
```

---

# ▶️ Running the RAG Pipeline

```bash
python -m rag_agent.main
```

---

# 🌐 Running FastAPI Server

```bash
uvicorn api.app:app --reload
```

---

# 📄 Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# 📥 Example API Request

```json
{
  "question": "How well does this candidate match the Python developer role?"
}
```

---

# 📤 Example Structured Output

```json
{
  "answer": "The resume highlights skills in Python, SQL, and Power BI. The candidate is missing experience with AWS.",

  "fit_score": 60,

  "matching_skills": [
    "Python",
    "SQL"
  ],

  "missing_skills": [
    "AWS"
  ],

  "seven_day_plan": [
    "Day 1: Learn AWS basics",
    "Day 2: Build mini cloud project"
  ],

  "citations": [
    "[SOURCE: filename.pdf]"
  ],

  "human_review_flag": false
}
```

---

# 🧪 Running Evaluation Tests

```bash
pytest
```

OR

```bash
python evaluation/run_tests.py
```

---

# 📸 Demo Walkthrough

The project demo includes:
- Resume loading
- ChromaDB retrieval pipeline
- Structured JSON outputs
- Validation and retry handling
- Prompt injection blocking
- Safety filtering
- FastAPI endpoint testing
- Evaluation testing workflow

---

# ⚠️ Known Limitations

- Small local models may occasionally generate malformed JSON
- Retrieval quality depends on document quality
- Local LLMs may hallucinate occasionally
- Not intended for hiring automation decisions
- Not intended for medical or legal advice

---

# 🚀 Future Improvements

- Streaming responses
- Better evaluation metrics
- Docker deployment
- Authentication layer
- Frontend UI integration
- Cloud deployment support
- Hybrid Search
- Re-ranking pipelines
- Multi-agent workflows
- AI observability integration

---

# 👩‍💻 Author

Yashaswini R

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.