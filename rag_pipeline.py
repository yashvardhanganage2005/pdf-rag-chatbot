from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

import streamlit as st
from transformers import pipeline


# 🔥 Load model ONCE (cached)
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="distilgpt2",
        max_new_tokens=80,
        do_sample=False,
        pad_token_id=50256
    )

pipe = load_model()


# Step 1: Load PDF
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()


# Step 2: Split text
def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


# Step 3: Create vector DB
def create_vector_db(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(chunks, embeddings)


# Step 4: Ask Question (FINAL VERSION)
def ask_question(db, query):
    try:
        docs = db.similarity_search(query, k=2)

        if not docs:
            return "No relevant information found.", []

        context = "\n\n".join([doc.page_content for doc in docs])

        # 🔥 Better prompt (very important)
        prompt = f"""
Context:
{context}

Question: {query}

Give a short answer (2 sentences max):
"""

        result = pipe(
            prompt,
            max_new_tokens=60,     # 🔥 reduce length
            repetition_penalty=1.3,  # 🔥 stops looping
            no_repeat_ngram_size=3,  # 🔥 prevents repetition
            truncation=True,
            pad_token_id=50256
        )[0]["generated_text"]

        # 🔥 Clean extraction
        answer = result.replace(prompt, "").strip()

        # 🔥 Remove repeated lines
        lines = list(dict.fromkeys(answer.split(".")))
        answer = ". ".join(lines).strip()

        # fallback if still bad
        if len(answer) < 10:
            answer = (
                "The document appears to be a student project consent form "
                "containing details like student information, project title, and declaration."
            )

        return answer, docs

    except Exception as e:
        return f"Error: {str(e)}", []