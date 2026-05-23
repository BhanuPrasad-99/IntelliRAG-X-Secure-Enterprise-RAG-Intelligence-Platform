import streamlit as st
import requests

st.set_page_config(
    page_title="IntelliRAG-X",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 IntelliRAG-X")
st.subheader("Secure Enterprise RAG Assistant")

# Sidebar
st.sidebar.title("🔐 Access Control")

role = st.sidebar.selectbox(
    "Select User Role",
    ["admin", "finance", "hr", "engineering"]
)

query = st.text_area(
    "Enter your enterprise query",
    placeholder="Show failed login attempts in finance systems..."
)

if st.button("Run Query"):
    
    payload = {
        "query": query,
        "user_role": role,
        "top_k": 5
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/query",
            json=payload
        )

        data = response.json()

        st.success("Query Processed Successfully")

        # Answer
        st.markdown("## 📌 AI Response")
        st.write(data["answer"])

        # Confidence
        st.markdown("## 🎯 Confidence")

        confidence = data["confidence_score"]

        st.progress(int(confidence))

        st.write(
            f'{data["confidence_level"]} Confidence '
            f'({confidence:.2f}%)'
        )

        # Citations
        st.markdown("## 📚 Citations")

        for citation in data["citations"]:
            st.info(citation)

        # Sources
        st.markdown("## 📂 Retrieved Sources")

        for source in data["retrieved_sources"]:
            st.json(source)

        # Trace
        st.markdown("## 🔍 Retrieval Trace")
        st.json(data["retrieval_trace"])

    except Exception as e:
        st.error(f"Error: {e}")