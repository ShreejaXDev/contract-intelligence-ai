# AI-Powered Contract Intelligence & Risk Scoring

## Overview

AI-Powered Contract Intelligence & Risk Scoring is an NLP-based system designed to automatically analyze legal contracts.

The system enables users to upload contract PDFs, extract key entities, identify important legal clauses, calculate risk scores, perform semantic search, and interact with contracts through a chatbot powered by Retrieval-Augmented Generation (RAG).

---

## Project Objectives

- Automate contract analysis
- Extract important legal information
- Identify risky contract clauses
- Enable semantic contract search
- Provide contract question-answering using LLMs

---

## Features

### 1. PDF Upload
Users can upload legal contracts in PDF format.

### 2. Contract Text Extraction
Extract text from uploaded PDF documents.

### 3. Named Entity Recognition (NER)
Identify:
- Organizations
- Dates
- Monetary Values
- Locations

### 4. Legal Clause Classification
Detect important clauses such as:
- Termination
- Confidentiality
- Liability
- Payment Terms

### 5. Risk Scoring
Generate a risk score based on potentially unfavorable contract terms.

### 6. Semantic Search
Search contract content using embeddings and vector similarity.

### 7. RAG-based Contract Chatbot
Ask natural language questions about the contract and receive context-aware answers.

---

## Tech Stack

### Backend
- Python
- FastAPI

### Frontend
- Streamlit

### NLP & Machine Learning
- spaCy
- Hugging Face Transformers
- Sentence Transformers

### Vector Database
- ChromaDB

### RAG Framework
- LangChain

### PDF Processing
- PyMuPDF
- pdfplumber

---

## Project Structure

```text
contract-intelligence-ai/
├── data/
├── notebooks/
├── src/
│   ├── ingestion/
│   ├── ner/
│   ├── classification/
│   ├── embeddings/
│   ├── rag/
│   └── utils/
├── api/
├── frontend/
├── models/
├── tests/
├── docker/
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/ShreejaXDev/contract-intelligence-ai.git
cd contract-intelligence-ai
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Open API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Current API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | / | API Status |
| POST | /upload | Upload Contract |
| GET | /analyze | Analyze Contract |
| GET | /chat | Contract Chatbot |

---

## Future Enhancements

- Advanced Risk Scoring Engine
- Clause-Level Risk Detection
- ChromaDB Vector Search
- Production RAG Pipeline
- LLM-Powered Contract Insights

---

## Team Project

This project is being developed collaboratively using GitHub, feature branches, pull requests, and modular architecture.