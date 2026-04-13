# 📄 PDF RAG Chatbot

An intelligent **Retrieval-Augmented Generation (RAG)** based chatbot that allows users to upload PDF documents and ask questions based on their content.

---

## 🚀 Overview

This project combines **document retrieval + language models** to generate accurate, context-aware answers from PDFs.

Instead of guessing answers, the system:

1. Extracts content from PDFs
2. Converts text into embeddings
3. Stores them in a vector database
4. Retrieves relevant chunks
5. Generates answers using an LLM

---

## 🧠 Features

* 📂 Upload multiple PDF files
* 🔍 Semantic search using FAISS
* 💬 Interactive chat interface (Streamlit)
* 📌 Source-based answers (context-aware)
* ⚡ Fast local inference (no API required)

---

## 🏗️ Architecture

```text
PDF → Text Extraction → Chunking → Embeddings → FAISS Vector DB
                                      ↓
                               User Query
                                      ↓
                          Similarity Search (Top-K)
                                      ↓
                         Context + Prompt → LLM → Answer
```

---

## 🛠️ Tech Stack

| Component       | Technology                         |
| --------------- | ---------------------------------- |
| Language        | Python                             |
| Framework       | Streamlit                          |
| RAG Pipeline    | LangChain                          |
| Vector Database | FAISS                              |
| Embeddings      | Sentence Transformers              |
| LLM             | HuggingFace (DistilGPT2 / FLAN-T5) |

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yashvardhanganage2005/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 📸 Demo

Upload a PDF → Ask a question → Get answers with source context.

---

## ⚠️ Limitations

* Uses lightweight local models (may produce less accurate answers)
* No long-term memory between sessions
* Performance depends on system hardware

---

## 🔮 Future Improvements

* 🔥 Integrate **Mistral (Ollama)** for better reasoning
* 🧠 Add conversational memory
* 🎨 Improve UI/UX (ChatGPT-like interface)
* ☁️ Deploy on cloud (Streamlit Cloud / Render)

---

## 📌 Learning Outcomes

* Implemented **RAG architecture**
* Understood **vector embeddings & semantic search**
* Built an **end-to-end AI application**
* Integrated **LLMs with real-world data**

---

## 👨‍💻 Author

**Yashvardhan Ganage**
B.Tech – CSE IoT and IS
Manipal University Jaipur
**Pragati Mohan**
B.Tech – CSE IoT and IS
Manipal University Jaipur

---

## ⭐ Acknowledgements

* LangChain
* HuggingFace
* Streamlit
* FAISS

---
