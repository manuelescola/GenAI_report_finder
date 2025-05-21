# main.py
import streamlit as st
from app.retriever import get_relevant_reports

st.title("🔍 GenAI Report Finder")
query = st.text_input("Describe what you're looking for:")

if st.button("Find Report") and query:
    with st.spinner("Searching..."):
        results = get_relevant_reports(query)
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            st.subheader(meta["name"])
            st.write(doc)