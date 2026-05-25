# Career Launch Agent

A production-grade AI-powered Career Launch Agent built using:

- RAG (Retrieval-Augmented Generation)
- ChromaDB Vector Database
- Sentence Transformers
- Ollama + Qwen2.5
- FastAPI
- Structured JSON Outputs
- Pydantic Validation
- Safety Guardrails

---

# Features

- Resume and Job Description Analysis
- Semantic Retrieval using ChromaDB
- Structured JSON Responses
- Retry Handling for Invalid Outputs
- Prompt Injection Detection
- Human Review Escalation
- FastAPI Backend API
- Safety Topic Detection
- Golden Test Evaluation Suite

---

# Project Architecture

```text
User Query
    ↓
Retriever
    ↓
ChromaDB
    ↓
Qwen2.5 via Ollama
    ↓
Structured JSON
    ↓
Pydantic Validation
    ↓
Safety Filters
    ↓
FastAPI Response
Project Structure
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
├── README.md
├── requirements.txt
├── pyproject.toml
└── uv.lock
Installation
Clone Repository
git clone <your-repository-url>
cd career-launch-agent
Create Virtual Environment
uv venv
Activate Virtual Environment
Windows PowerShell
.venv\Scripts\activate
Mac/Linux
source .venv/bin/activate
Install Dependencies
uv sync
Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull Qwen Model
ollama pull qwen2.5:3b
Running the RAG Pipeline
python -m rag_agent.main
Running FastAPI Server
uvicorn api.app:app --reload
Open Swagger UI
http://127.0.0.1:8000/docs
Example API Request
{
  "question": "How well does this candidate match the Python developer role?"
}
Example Structured Output
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
Running Evaluation Tests
python evaluation/run_tests.py
Safety Features
Prompt Injection Detection
Output Validation
Human Review Escalation
Medical/Legal/Confidential Topic Filtering
Structured Output Validation
Retry Handling for Malformed JSON
Evaluation & Reliability

The project includes:

Golden test evaluation suite
Structured schema validation
Retry logic for malformed outputs
Output normalization
Failure documentation
Known Limitations
Small local models may occasionally generate malformed JSON
Retrieval quality depends on document quality
Local models may hallucinate occasionally
Not intended for hiring automation decisions
Not intended for medical or legal advice
Tech Stack
Python 3.11+
FastAPI
ChromaDB
SentenceTransformers
Ollama
Qwen2.5
Pydantic
Uvicorn
uv
Future Improvements
Streaming responses
Better evaluation metrics
Docker deployment
Authentication layer
Frontend UI integration
Cloud deployment support
Demo Walkthrough

The project demo includes:

Resume loading
Retrieval pipeline
Structured JSON outputs
Validation and retry handling
Safety filtering
FastAPI endpoint testing
Author

Yashaswini R

License

This project is intended for educational and portfolio purposes.