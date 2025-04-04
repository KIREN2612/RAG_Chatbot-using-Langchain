# RAG Chatbot using LangChain

## 📌 Project Overview
This project is an implementation of a **Retrieval-Augmented Generation (RAG) chatbot** using **LangChain**, designed to efficiently retrieve relevant context from uploaded PDFs and generate meaningful responses based on user queries. The chatbot leverages **Large Language Models (LLMs)** to enhance knowledge retrieval and provide accurate, context-aware answers.

## 🎯 Purpose of the Project
This chatbot was built as part of my learning journey into **RAG-based architectures**, **LangChain**, and **LLM-powered applications**. The goal was to:
- Understand **document-based Q&A systems** using embeddings and vector stores.
- Learn how to integrate **LLMs with external knowledge sources** for better contextual awareness.
- Explore **LangChain** and its components to build practical AI-driven applications.
- Experiment with **FastAPI** for the backend and **Gradio** for an intuitive frontend.

## ⚙️ Features
✔ **PDF Upload Support** – Users can upload PDF files, and the chatbot retrieves relevant context from them.
✔ **RAG-Powered Responses** – Uses LangChain to fetch relevant information from PDFs before generating answers.
✔ **Gradio Frontend** – A simple and interactive UI for seamless interactions.
✔ **FastAPI Backend** – Ensures efficient request handling and model predictions.
✔ **Scalable Architecture** – Can be extended with different LLMs and vector stores.

## 🚀 Tech Stack
- **LangChain** – Framework for building LLM applications with knowledge retrieval.
- **OpenAI/LLM Models** – For generating responses based on retrieved context.
- **FAISS / ChromaDB** – Used as vector stores to store and retrieve embeddings.
- **FastAPI** – For handling API requests efficiently.
- **Gradio** – Provides a clean and easy-to-use interface for user interaction.
- **Python** – The core programming language for the implementation.

## 📂 Project Structure
```
RAG_Chatbot/
│── main.py                 # Backend API using FastAPI
│── gradio_frontend.py      # Gradio-based UI
│── # CHATBOT MODULE.py     # Handles chatbot logic
│── # MEMORY MANAGER MODULE.py  # Manages context retention
│── # PDF PROCESSING MODULE.py  # Extracts text from PDFs
│── # UTILS MODULE.py       # Helper functions
│── # MODEL SETUP MODULE.py # Loads and configures the LLM
│── requirements.txt        # List of dependencies
```

## 🛠️ Installation & Usage
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/KIREN2612/RAG_Chatbot-using-Langchain.git
cd RAG_Chatbot-using-Langchain
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Backend API
```bash
python main.py
```

### 4️⃣ Run the Frontend
```bash
python gradio_frontend.py
```

### 5️⃣ Open the Gradio UI and Start Chatting!
After running the frontend script, Gradio will provide a **local URL** where you can upload PDFs and interact with the chatbot.

## 📌 Future Enhancements
🔹 Improve response accuracy by integrating **more advanced vector databases**.<br>
🔹 Enable support for **multiple document formats (Word, TXT, etc.)**.<br>
🔹 Add **user authentication and session-based memory**.<br>
🔹 Explore **fine-tuned models** for domain-specific applications.<br>

## 📜 License
This project is open-source under the **Apache license 2.0**.

---
💡 **This project is a part of my ongoing exploration into LLM-based applications.** If you find it interesting, feel free to fork, contribute, or share feedback! 🚀

