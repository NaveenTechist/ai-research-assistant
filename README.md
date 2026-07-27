# AI Research & Knowledge Assistant

A production-ready AI Research & Knowledge Assistant built with FastAPI, ChromaDB, Sentence Transformers, TensorFlow, and Google Gemini. The application enables intelligent document processing, semantic search, Retrieval-Augmented Generation (RAG), document classification, document summarization, comparison, and analytics through a clean REST API.

---

# Features

- PDF Upload & Processing
- Background Document Processing
- Page-wise PDF Text Extraction
- Intelligent Text Chunking
- SentenceTransformer Embeddings
- ChromaDB Vector Database
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Citation-Based Question Answering
- Conversation Memory
- TensorFlow Document Classification
- Multi-Document Summarization
- Multi-Document Comparison
- System Analytics Dashboard
- Interactive Swagger Documentation

---

# Tech Stack

## Backend

- FastAPI
- Python 3.10

## AI & Machine Learning

- Google Gemini 2.5 Flash
- Sentence Transformers
- TensorFlow
- Scikit-learn

## Vector Database

- ChromaDB

## Database

- SQLite

## Document Processing

- PyMuPDF

---

# Project Structure

```text
ai-research-assistant/
│
├── config/
├── data/
│   ├── dataset/
│   ├── raw_documents/
│   └── vector_db/
│
├── models/
│
├── src/
│   ├── analytics/
│   ├── database/
│   ├── document_processing/
│   ├── ml/
│   ├── rag/
│   └── vector_store/
│
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/NaveenTechist/ai-research-assistant.git
```

## Navigate to Project

```bash
cd ai-research-assistant
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=sqlite:///./data/database.db
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
VECTOR_DB_DIR=data/vector_db
MODEL_PATH=models/tf_classifier.h5
```

---

# Run the Application

```bash
uvicorn main:app --reload
```

Open Swagger UI

```text
http://localhost:8000/docs
```

---

# API Endpoints

## Document Management

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/documents/upload` | Upload and process PDF documents |

---

## Search

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/search/semantic` | Perform semantic similarity search |
| POST | `/search/question` | Ask questions using Retrieval-Augmented Generation (RAG) |

---

## Analysis

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/analysis/summarize` | Generate document summaries |
| POST | `/analysis/compare` | Compare multiple documents |

---

## Analytics

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/analytics/metrics` | Retrieve system analytics |

---

# AI Processing Pipeline

```text
PDF Upload
      │
      ▼
Background Processing
      │
      ▼
PDF Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
SentenceTransformer Embeddings
      │
      ▼
ChromaDB Vector Storage
      │
      ▼
Semantic Retrieval
      │
      ▼
Google Gemini
      │
      ▼
Answer Generation with Citations
```

---

# Machine Learning Pipeline

```text
Training Dataset
        │
        ▼
Text Preprocessing
        │
        ▼
TensorFlow Model Training
        │
        ▼
Model Serialization
        │
        ▼
Automatic Document Classification
```

---

# Testing

Start the application.

```bash
uvicorn main:app --reload
```

Open Swagger UI.

```text
http://localhost:8000/docs
```

Upload the sample documents provided in the project:

- `rag-testing-pdf-1.pdf`
- `rag-testing-pdf-2.pdf`

These sample PDFs are included to help you test:

- Document Upload
- Semantic Search
- Question Answering (RAG)
- Document Summarization
- Document Comparison
- Analytics

You can also upload your own PDF documents for testing.

---

# API Documentation

Interactive Swagger Documentation

```text
http://localhost:8000/docs
```

---


**Naveen Yarramsetti**

GitHub

```text
https://github.com/NaveenTechist
```

LinkedIn

```text
https://linkedin.com/in/naveen-yarramsetti
