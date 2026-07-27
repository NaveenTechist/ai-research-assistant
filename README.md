# AI Research & Knowledge Assistant

A production-ready AI Research & Knowledge Assistant built with FastAPI, ChromaDB, Sentence Transformers, TensorFlow, and Google Gemini. The system enables intelligent document processing, semantic search, Retrieval-Augmented Generation (RAG), document summarization, comparison, analytics, and automatic document classification.

---

## Features

- PDF Upload & Processing
- Page-wise Text Extraction
- Intelligent Text Chunking
- SentenceTransformer Embeddings
- ChromaDB Vector Storage
- Semantic Search
- Hybrid Search
- Retrieval-Augmented Generation (RAG)
- Citation-based Question Answering
- TensorFlow Document Classification
- Multi-document Summarization
- Multi-document Comparison
- System Analytics
- Swagger API Documentation

---

## Tech Stack

### Backend

- FastAPI
- Python 3.10

### AI & NLP

- Google Gemini 2.5 Flash
- Sentence Transformers
- TensorFlow
- Scikit-learn

### Database

- SQLite
- ChromaDB

### Document Processing

- PyMuPDF

---

## Project Structure

```
ai-research-assistant/
│
├── config/
├── data/
├── models/
├── src/
│   ├── database/
│   ├── document_processing/
│   ├── ml/
│   ├── rag/
│   ├── vector_store/
│   └── analytics/
│
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/NaveenTechist/ai-research-assistant.git
```

Go into the project

```bash
cd ai-research-assistant
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file

```env
DATABASE_URL=sqlite:///./data/database.db
GOOGLE_API_KEY=YOUR_API_KEY
VECTOR_DB_DIR=data/vector_db
MODEL_PATH=models/tf_classifier.h5
```

---

## Run Project

```bash
uvicorn main:app --reload
```

Open Swagger

```
http://localhost:8000/docs
```

---

## API Endpoints

### Document

- POST `/documents/upload`

### Search

- POST `/search/semantic`
- POST `/search/question`

### Analysis

- POST `/analysis/summarize`
- POST `/analysis/compare`

### Analytics

- GET `/analytics/metrics`

---

## AI Pipeline

```
PDF Upload
      │
      ▼
PDF Parsing
      │
      ▼
Chunking
      │
      ▼
SentenceTransformer Embeddings
      │
      ▼
ChromaDB
      │
      ▼
Semantic Search
      │
      ▼
Gemini RAG
      │
      ▼
Answer with Citations
```

---

## Machine Learning Pipeline

```
Dataset
    │
    ▼
TensorFlow Training
    │
    ▼
Saved .h5 Model
    │
    ▼
Document Classification
```

---

## Testing

Swagger

```
http://localhost:8000/docs
```

---

## Future Improvements

- Conversation Memory
- Background Processing
- Authentication
- PostgreSQL Support
- Docker Deployment
- Cloud Storage
- Query Analytics Dashboard

---

**Naveen Yarramsetti**

GitHub
https://github.com/NaveenTechist

LinkedIn

https://linkedin.com/in/naveen-yarramsetti