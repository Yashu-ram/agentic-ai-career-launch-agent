# System Card — Career Launch Agent

---

# Overview

The Career Launch Agent is a production-style AI-powered RAG (Retrieval-Augmented Generation) system designed to analyze resumes against job descriptions and provide structured career guidance.

The system uses semantic retrieval, structured JSON outputs, safety guardrails, and validation layers to improve reliability and transparency.

---

# Intended Use

The system is intended for:

- Career guidance assistance
- Resume and job description comparison
- Skill gap analysis
- Learning roadmap generation
- Educational AI engineering demonstrations
- Portfolio and experimentation purposes

---

# Non-Intended Use

The system is NOT intended for:

- Hiring automation decisions
- Candidate rejection decisions
- Medical advice
- Legal advice
- Financial advice
- Confidential data analysis
- Production HR screening systems

Human oversight is recommended for all important decisions.

---

# Models Used

## LLM

- Qwen2.5:3b via Ollama

## Embedding Model

- all-MiniLM-L6-v2

## Vector Database

- ChromaDB

---

# System Architecture

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


Structured Output Schema

The system enforces structured outputs using Pydantic validation.

# Required fields:

answer
fit_score
matching_skills
missing_skills
seven_day_plan
citations
human_review_flag

Malformed outputs trigger retry handling and normalization logic.

# Safety Controls

The system includes several safety mechanisms:

Prompt Injection Defense

Detects suspicious prompts attempting to override instructions.

# Output Validation

Validates model responses before returning outputs.

Human Review Escalation

Flags potentially unsafe or sensitive outputs for human review.

Topic Filtering

#Detects:

medical topics
legal topics
confidential information
Structured Validation

# Uses Pydantic schema enforcement to validate outputs.

Data Handling
Local Processing

All inference and vector retrieval run locally.

No Permanent Storage

The system does not permanently store user prompts or outputs.

Document Usage

Uploaded resumes and job descriptions are used only for retrieval and response generation.

# Limitations

The system has several known limitations:

Small local models may occasionally generate malformed JSON
Retrieval quality depends on document quality
Local LLMs may hallucinate occasionally
Responses are limited by retrieved context
Safety filtering is keyword-based and not fully comprehensive
The system should not be used for high-stakes decision making
Evaluation

# The project includes:

Golden test suite
Retry handling
Failure normalization
Structured validation
Manual failure analysis
Human Oversight

The system is designed to support humans, not replace them.

Users should verify important outputs independently.

Future Improvements

# Potential future enhancements include:

Better evaluation metrics
Advanced guardrails
Cloud deployment
Authentication
Streaming responses
Frontend integration
Fine-tuned models
Author

Yashaswini R

License

Educational and portfolio use only.