# 📄 AI-Powered Contract Intelligence & Risk Scoring

An end-to-end AI-powered contract analysis system that automatically extracts, classifies, and analyzes legal contract clauses using Natural Language Processing (NLP) and Deep Learning.

The system enables users to upload contract PDFs, identify important clauses, classify them using a fine-tuned DistilBERT model, evaluate legal risks, extract key entities, and visualize the results through an interactive Streamlit dashboard.

---

## 🚀 Features

### 📄 PDF Contract Processing
- Upload legal contracts in PDF format
- Extract text using **pdfplumber**
- Automatically process contracts of varying lengths

### ✂️ Intelligent Clause Extraction
- Automatically split contracts into individual clauses
- Regex-based clause detection
- Supports structured legal documents

### 🤖 AI Clause Classification
- Fine-tuned **DistilBERT** model
- Predicts contract clause categories
- Returns prediction confidence
- Displays Top-3 predicted categories

Supported Categories:

- General
- Legal
- Payment
- Termination
- Confidentiality
- Liability
- Employment
- Property
- Performance
- Intellectual Property

---

### ⚠️ Risk Assessment

Automatically assigns risk levels based on detected clause type.

Risk Levels:

- 🔴 High Risk
- 🟡 Medium Risk
- 🟢 Low Risk

Each risk includes an AI-generated explanation to help users understand potential legal concerns.

---

### 🧠 Named Entity Recognition (NER)

Extracts important entities from contracts using **SpaCy**.

Supported Entities:

- Organizations
- People
- Dates
- Money
- Locations

---

### 📊 Confidence Scores

Every prediction includes:

- Prediction confidence
- Top-3 possible categories

Example:

| Category | Confidence |
|----------|------------|
| Payment | 97.42% |
| Legal | 1.81% |
| General | 0.77% |

---

### 🌐 FastAPI Backend

REST API built using FastAPI.

Endpoints include:

- Upload Contract
- Analyze Contract
- Chat Endpoint (Ready for Extension)

Returns structured JSON responses for frontend integration.

---

### 🎨 Streamlit Dashboard

Interactive frontend providing:

- PDF Upload
- Contract Summary
- Risk Summary
- Clause Classification
- Confidence Scores
- Named Entity Extraction
- AI Recommendations
- Expandable Clause Details

---

## 🏗 Project Architecture

```
                 Streamlit Dashboard
                         │
                         ▼
                  Upload Contract
                         │
                         ▼
                    FastAPI Backend
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   PDF Parser      Clause Splitter   DistilBERT
                                           │
                                           ▼
                                   Confidence Score
                                           │
                                           ▼
                                    Risk Analyzer
                                           │
                                           ▼
                                   Named Entity Recognition
                                           │
                                           ▼
                                     JSON Response
                                           │
                                           ▼
                                 Streamlit Dashboard
```

---

## 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- PyTorch
- Hugging Face Transformers
- DistilBERT

### NLP

- SpaCy
- pdfplumber
- Regex

### Backend

- FastAPI
- Uvicorn

### Frontend

- Streamlit

### Data Processing

- Pandas
- NumPy

### Model Training

- DistilBERT
- Label Encoder (Scikit-learn)

---

## 📂 Project Structure

```
contract-intelligence-ai/

│
├── api/
│   ├── main.py
│   └── routes/
│       ├── upload.py
│       ├── analyze.py
│       └── chat.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── saved_model/
│
├── src/
│   ├── classification/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── ner/
│   ├── risk/
│   └── services/
│
├── uploads/
│
├── streamlit_app.py
├── label_encoder.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/contract-intelligence-ai.git

cd contract-intelligence-ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

Frontend:

```
http://localhost:8501
```

---

## 📈 Workflow

1. Upload Contract PDF
2. Extract Contract Text
3. Split into Clauses
4. Classify using DistilBERT
5. Calculate Confidence Score
6. Perform Risk Analysis
7. Extract Named Entities
8. Display Interactive Results

---

## 📊 Example Output

### Risk Summary

```
High Risk : 5

Medium Risk : 2

Low Risk : 12
```

---

### Clause Prediction

| Clause | Category | Confidence | Risk |
|---------|-----------|------------|------|
| Termination | Termination | 98.6% | High |
| Payment | Payment | 96.3% | Medium |
| Confidentiality | Confidentiality | 97.8% | High |

---

### Named Entities

```
Organizations

People

Dates

Money

Locations
```

---

## 🎯 Future Improvements

- Legal-BERT Integration
- OCR Support for Scanned Contracts
- Multi-language Contract Analysis
- AI Chatbot for Contract Q&A
- Contract Comparison
- Automatic Clause Recommendation
- Risk Heatmap Visualization
- Docker Deployment
- Cloud Deployment (AWS/Azure)

---

## 💼 Resume Highlights

✔ End-to-End AI Application

✔ Transformer-based NLP

✔ PDF Processing

✔ Contract Intelligence

✔ Named Entity Recognition

✔ Risk Assessment

✔ FastAPI REST API

✔ Streamlit Dashboard

✔ Deep Learning

✔ Machine Learning

---

## 👩‍💻 Author

**Shreeja Upadhyay**

B.Tech Computer Engineering

CHARUSAT University

GitHub: https://github.com/ShreejaXDev

---

## ⭐ If you found this project useful, consider giving it a star!