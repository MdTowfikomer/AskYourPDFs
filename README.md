# 📘 AskYourPDFs — AI-Powered PDF Q&A using RAG

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Qdrant](https://img.shields.io/badge/Vector%20DB-Qdrant-FF6F00.svg?logo=qdrant&logoColor=white)](https://qdrant.tech)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Upload PDFs and ask context-aware questions powered by Retrieval-Augmented Generation (RAG).  
> Combines **Streamlit**, **Qdrant**, **LlamaIndex**, **Cohere embeddings**, and **OpenRouter (DeepSeek v3.1)** to turn static documents into interactive knowledge.

---

## 🧠 Overview

**AskYourPDFs** allows you to interact with your PDFs like a chatbot. It extracts content from uploaded PDFs, stores embeddings in a **Qdrant** vector database, and retrieves relevant chunks when you ask a question. The context is then processed by **DeepSeek v3.1** (via OpenRouter) for precise, source-grounded answers.

> 💡 Think of it as "ChatGPT for your own documents."

---

## 🧩 Tech Stack

| Category | Technology Used |
|----------|-----------------|
| 🖥️ Frontend | Streamlit |
| 🧠 Embedding Model | Cohere |
| 🗂️ Retrieval Framework | LlamaIndex |
| 🧮 Vector Database | Qdrant (Docker container) |
| 🗣️ Language Model | DeepSeek v3.1 via OpenRouter |
| ⚙️ Backend | FastAPI, Uvicorn |
| 🔄 Workflow Engine | Inngest |
| 🧰 Dev Tools | Docker Desktop |

---

## 🗂 Architecture

```
[User Uploads PDFs]
        ↓
[Text Extraction & Chunking]
        ↓
[Embeddings Generation via Cohere]
        ↓
[Stored in Qdrant DB]
        ↓
[User Asks Question]
        ↓
[Retrieve Relevant Chunks]
        ↓
[DeepSeek v3.1 (OpenRouter) Generates Answer]
        ↓
[Streamlit UI Displays Answer]
```

---

## ⚡ Key Features

- 📤 Upload multiple PDFs seamlessly
- 🧾 Extract and chunk text intelligently
- 🧠 Generate embeddings using Cohere
- 🔍 Store and retrieve using Qdrant
- 💬 Query with context using DeepSeek v3.1 via OpenRouter
- 🧱 Modular Python code: `data_loader.py`, `vector_db.py`, `streamlit_app.py`
- ⚡ Fast, real-time responses

> **[Future]** Multi-modal RAG, voice input, summarization timelines, and more.

---

## ⚙️ Local Setup

### 1️⃣ Install Dependencies

```bash
pip install fastapi inngest llama-index-core llama-index-readers-file python-dotenv qdrant-client uvicorn streamlit openai
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Services

**Start Qdrant DB (Docker):**
```bash
docker run -d --name qdrantRagDb -p 6333:6333 -v "$(pwd)/qdrant_storage:/qdrant/storage" qdrant/qdrant
```

**Run FastAPI Server:**
```bash
uv run uvicorn main:app --reload
```

**Run Inngest Dev Server:**
```bash
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
```

**Launch Streamlit App:**
```bash
uv run streamlit run streamlit_app.py
```

### 3️⃣ Environment Variables

Create a `.env` file in your project root:

```env
COHERE_API_KEY=your_cohere_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

---

## 🌐 Deployment

Currently deployed on **Streamlit Cloud**.

**Future deployment options:**
- Dockerized deployment on VPS/Cloud VM
- Vercel or Render for scaling
- AWS/GCP/Azure cloud services

---

## 🗃 Folder Structure

```
.
├── main.py             # FastAPI backend
├── streamlit_app.py    # Streamlit frontend
├── data_loader.py      # PDF extraction and processing
├── vector_db.py        # Qdrant interaction
├── .env                # Environment variables (not tracked)
├── requirements.txt    # Python dependencies
├── qdrant_storage/     # Local Qdrant DB storage
├── LICENSE             # MIT License
└── README.md           # This file
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests
- Suggest improvements

**Planned improvements:**
- Multi-modal support (images, tables)
- Voice input integration
- Summarization timelines
- User authentication
- Enhanced UI/UX

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

Built with:
- [Streamlit](https://streamlit.io)
- [LlamaIndex](https://www.llamaindex.ai)
- [Qdrant](https://qdrant.tech)
- [Cohere](https://cohere.ai)
- [OpenRouter](https://openrouter.ai)

---

**Made with ❤️ for the AI community**
