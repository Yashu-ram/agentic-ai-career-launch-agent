from fastapi import FastAPI
from pydantic import BaseModel

from rag_agent.main import ask_rag


app = FastAPI()


class QueryRequest(BaseModel):

    question: str


@app.post("/analyze")

def analyze(request: QueryRequest):

    result = ask_rag(request.question)

    return result