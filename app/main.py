# -*- coding: utf-8 -*-
from fastapi import FastAPI
from pydantic import BaseModel

from app.pipeline import critique, draft, retrieve

app = FastAPI(title="proposal-review-agent-demo")


class RunIn(BaseModel):
    topic: str = "耳机包装破损的改进方案"


@app.get("/health")
def health():
    return {"status": "ok", "demo": True}


@app.post("/run")
def run(body: RunIn):
    hits = retrieve(body.topic)
    text = draft(body.topic, hits)
    critic = critique(text, hits)
    return {
        "topic": body.topic,
        "hits": hits,
        "draft": text,
        "critic": critic,
        "ship": critic["pass"],
        "note": "critic.pass=false 时不得外发。本 Demo 无真实客户通道。",
    }
