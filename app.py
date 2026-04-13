import streamlit as st
from rag_pipeline import load_pdf, split_text, create_vector_db, ask_question

st.set_page_config(page_title="PDF Chatbot", layout="wide")

# Sidebar
st.sidebar.title("📄 Upload Documents")
uploaded_files = st.sidebar.file_uploader(
    "Upload PDF files", type="pdf", accept_multiple_files=True
)

# Title
st.title("💬 Chat with your PDF")

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "db" not in st.session_state:
    st.session_state.db = None

if "last_sources" not in st.session_state:
    st.session_state.last_sources = []


# Process PDFs
if uploaded_files:
    all_docs = []

    with st.spinner("Processing PDFs..."):
        for file in uploaded_files:
            with open(file.name, "wb") as f:
                f.write(file.read())

            docs = load_pdf(file.name)
            all_docs.extend(docs)

        chunks = split_text(all_docs)
        st.session_state.db = create_vector_db(chunks)

    st.sidebar.success("✅ PDFs processed successfully!")


# Chat input
query = st.chat_input("Ask a question about your PDF...")

if query and st.session_state.db:
    with st.spinner("Thinking..."):
        answer, sources = ask_question(st.session_state.db, query)

    # Save chat + sources
    st.session_state.chat_history.append(("user", query))
    st.session_state.chat_history.append(("bot", answer))
    st.session_state.last_sources = sources


# Display chat
for role, message in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)


# Show sources (optimized)
if st.session_state.last_sources:
    st.markdown("---")
    st.subheader("📌 Source Snippets")

    for i, doc in enumerate(st.session_state.last_sources):
        st.write(f"**Source {i+1}:**")
        st.write(doc.page_content[:200])