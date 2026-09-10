# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient
from app.main import app
from app.pipeline import critique

c = TestClient(app)


def test_all():
    assert c.get("/health").json()["status"] == "ok"
    r = c.post("/run", json={"topic": "耳机包装破损"}).json()
    assert r["hits"] and r["critic"]["pass"] is True
    bad = critique("我们保证退货率降到 1%。", r["hits"])
    assert bad["pass"] is False
    print("SMOKE_OK")


if __name__ == "__main__":
    test_all()
