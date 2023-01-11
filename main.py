import json

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Question(BaseModel):
    question: str
    choices: List[str]
    correct: str


with open('data.json') as f:
    data = json.load(f)


app = FastAPI()


@app.get("/")
async def search(q: str = ""):
    resp = [question for question in data if q.lower() in question["question"].lower()]
    return resp
