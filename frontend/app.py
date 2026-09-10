# -*- coding: utf-8 -*-
import os
import httpx
import streamlit as st

API = os.environ.get("API_BASE", "http://127.0.0.1:8013")
st.set_page_config(page_title="方案多智能体 Demo")
st.title("方案起草多智能体（检索 / 起草 / 审稿）")
try:
    ok = httpx.get(API + "/health", timeout=2).json().get("status") == "ok"
except Exception:
    ok = False
st.sidebar.write("后端服务在线" if ok else "后端未启动")
topic = st.text_input("任务", "耳机包装破损的改进方案")
if st.button("跑一遍") and topic.strip():
    data = httpx.post(API + "/run", json={"topic": topic}, timeout=10).json()
    st.subheader("检索")
    st.json(data.get("hits"))
    st.subheader("初稿")
    st.markdown(data.get("draft") or "")
    st.subheader("审稿")
    st.json(data.get("critic"))
    st.write("可外发" if data.get("ship") else "驳回，不可外发")
