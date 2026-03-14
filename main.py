from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.ai_query_engine import process_query
from analytics.forensic_insights import most_contacted, suspicious_messages

app = FastAPI()

# Enable browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "UFDR AI Investigation System Running"}


@app.post("/query")
def ask_query(q: Query):

    result = process_query(q.question)

    return {"result": result}


@app.get("/insights")
def insights():

    most_contacted()
    suspicious_messages()

    return {"status": "analysis complete"}