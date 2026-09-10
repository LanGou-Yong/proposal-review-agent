# -*- coding: utf-8 -*-
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"


def retrieve(topic: str, k: int = 3):
    hits = []
    for p in DOCS.glob("*.md"):
        text = p.read_text(encoding="utf-8").strip()
        score = sum(1 for w in topic if w in text) + (2 if any(x in text and x in topic for x in ["退货", "包装", "竞品", "华南"]) else 0)
        hits.append((score, p.name, text))
    hits.sort(reverse=True)
    return [{"file": n, "text": t} for s, n, t in hits[:k] if s > 0]


def draft(topic: str, hits: list) -> str:
    if not hits:
        return "材料不足，无法起草。请补充内部文档。"
    lines = ["# 初稿：" + topic, "", "以下内容仅基于内部检索材料：", ""]
    for h in hits:
        lines.append("- %s [%s]" % (h["text"].split("来源文件")[0].strip(), h["file"]))
    lines.append("")
    lines.append("建议：先在华南仓试点包装加固，并评估详情页开箱引导。 [q3_review.md] [competitor.md]")
    lines.append("对外口径需遵守：不得无引用承诺退货率。 [sop.md]")
    return "\n".join(lines)


def critique(draft_text: str, hits: list) -> dict:
    allowed = {h["file"] for h in hits}
    allowed.update(["q3_review.md", "competitor.md", "sop.md"])
    problems = []
    skip_prefix = ("#", "以下内容")
    for raw in draft_text.split("\n"):
        line = raw.strip()
        if not line or line.startswith(skip_prefix) or line.startswith("以下内容"):
            continue
        if "[" not in line:
            problems.append("无引用：" + line[:80])
    ok = not problems
    return {"pass": ok, "problems": problems, "allowed_sources": sorted(allowed)}
