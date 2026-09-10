# 方案起草多智能体（脱敏 Demo）

最小链路：检索内部材料 → 起草带引用初稿 → 审稿检查无出处句子并驳回。

这是公开技术验证，不是自动投标系统。材料是虚构的内部摘录。

## 30 秒看懂

| 步骤 | 谁做 | 约束 |
|---|---|---|
| 检索 | retriever | 只从 docs/ 取片段，带来源文件名 |
| 起草 | writer | 关键句必须带 [来源] |
| 审稿 | critic | 没有引用的断言 → 驳回，不直接外发 |

## 刻意没做

- 自动发给客户
- 全网搜索
- 8 个角色的 AutoGPT

## 快速开始

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python start_demo.py
```

浏览器：http://localhost:8513
