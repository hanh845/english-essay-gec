# English Essay Grammar Error Detection System

## 1. Introduction

This project is a backend system for detecting grammatical errors in English essays using Natural Language Processing (NLP) and Machine Learning.

The system allows users to:

- Upload English essay PDFs
- Extract text from PDF files
- Automatically split text into sentences
- Detect grammar mistakes using AI/NLP models
- Store prediction results in PostgreSQL
- Generate user-based statistics and analytics
- Manage document versions
- Provide REST APIs for frontend integration

---

# 2. Technologies Used

| Component | Technology |
|---|---|
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| NLP Model | Transformers / BERT |
| Deep Learning | PyTorch |
| PDF Processing | pdfplumber |
| Sentence Tokenization | NLTK |
| API Testing | Postman |

---

# 3. Project Structure

```text
english-essay-gec/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── documents.py
│   │       ├── statistics.py
│   │       └── training.py
│   │
│   ├── core/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── authors.py
│   │   ├── document.py
│   │   ├── sentence.py
│   │   ├── prediction.py
│   │   ├── document_version.py
│   │   ├── document_author.py
│   │   ├── models.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── pdf_parser_service.py
│   │   ├── prediction_service.py
│   │   └── sentence_service.py
│   │
│   ├── ml/
│   │   ├── dataset.py
│   │   ├── inference.py
│   │   └── train_bert_gec.py
│   │
│   └── main.py
│
├── data/
│   ├── lang8/
│   └── uploads/
│
├── sql/
│   └── schema.py
│
├── requirements.txt
├── English Essay Error Detection API.postman_collection.json
└── README.md
```

---

# 4. System Requirements

- Python 3.11+
- PostgreSQL 14+
- pip
- virtualenv

---

# 5. Environment Setup

## 5.1 Clone the Repository

```bash
git clone <repository-url>

cd english-essay-gec
```

---

## 5.2 Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 5.3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 6. PostgreSQL Configuration

## 6.1 Create Database

```sql
CREATE DATABASE essay_gec;
```

---

## 6.2 Run Database Schema

```bash
psql -U postgres -d essay_gec -f schema.sql
```

You can also execute the SQL file directly in pgAdmin.

---

# 7. Seed Initial Authors Data

```sql
INSERT INTO authors (
    author_id,
    name,
    email,
    created_at
)
VALUES
(
    '11111111-1111-1111-1111-111111111111',
    'Nguyen Van A',
    'nguyenvana@gmail.com',
    CURRENT_TIMESTAMP
),
(
    '22222222-2222-2222-2222-222222222222',
    'Tran Thi B',
    'tranthib@gmail.com',
    CURRENT_TIMESTAMP
);
```

---

# 8. Run the Application

```bash
uvicorn app.main:app --reload
```

Swagger API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 9. Database Design

## 9.1 authors

Stores student/author information.

| Column | Type |
|---|---|
| author_id | UUID |
| name | VARCHAR |
| email | VARCHAR |
| created_at | TIMESTAMP |

---

## 9.2 documents

Stores uploaded PDF metadata.

| Column | Type |
|---|---|
| document_id | UUID |
| title | VARCHAR |
| file_path | TEXT |
| file_type | VARCHAR |
| created_at | TIMESTAMP |

---

## 9.3 document_authors

Many-to-many relationship between authors and documents.

| Column | Type |
|---|---|
| author_id | UUID |
| document_id | UUID |

---

## 9.4 document_versions

Stores extracted text from PDFs.

| Column | Type |
|---|---|
| version_id | UUID |
| document_id | UUID |
| extracted_text | TEXT |
| extraction_method | VARCHAR |
| created_at | TIMESTAMP |

---

## 9.5 sentences

Stores tokenized sentences.

| Column | Type |
|---|---|
| sentence_id | UUID |
| document_id | UUID |
| version_id | UUID |
| content | TEXT |
| position | INTEGER |
| is_clean | BOOLEAN |
| created_at | TIMESTAMP |

---

## 9.6 predictions

Stores grammar correction predictions.

| Column | Type |
|---|---|
| prediction_id | UUID |
| sentence_id | UUID |
| corrected_text | TEXT |
| confidence | FLOAT |
| label | INTEGER |
| created_at | TIMESTAMP |

---

# 10. System Relationships

```text
Authors
   ↕
document_authors
   ↕
Documents
   ↓
DocumentVersions
   ↓
Sentences
   ↓
Predictions
```

---

# 11. Main APIs

| Endpoint | Method | Description |
|---|---|---|
| /authors | POST | Create new author |
| /documents/upload | POST | Upload PDF essay |
| /documents/{id}/detect | POST | Detect grammar errors |
| /documents/{id}/errors | GET | Get all detected errors |
| /statistics/user/{author_id} | GET | Get user statistics |

---

# 12. Upload PDF API

## Endpoint

```text
POST /documents/upload
```

## Form-data Parameters

| Key | Type |
|---|---|
| title | Text |
| author_id | Text |
| file | File |

Example:

| Key | Value |
|---|---|
| title | Essay 1 |
| author_id | 11111111-1111-1111-1111-111111111111 |
| file | essay.pdf |

---

# 13. System Processing Pipeline

```text
Upload PDF
    ↓
Save Document
    ↓
Save Author Relationship
    ↓
Extract PDF Text
    ↓
Save Document Version
    ↓
Sentence Tokenization
    ↓
Save Sentences
    ↓
Run NLP Model
    ↓
Save Predictions
    ↓
Statistics & Reporting
```

---

# 14. Grammar Error Detection

## Endpoint

```text
POST /documents/{document_id}/detect
```

## Functions

- Load all document sentences
- Run NLP prediction model
- Detect grammatical errors
- Generate corrected sentences
- Save predictions into database

---

# 15. Get All Document Errors

## Endpoint

```text
GET /documents/{document_id}/errors
```

## Functions

- Join sentences and predictions tables
- Return all detected grammar errors
- Display original and corrected sentences

---

# 16. User Statistics API

## Endpoint

```text
GET /statistics/user/{author_id}
```

## Functions

- Total uploaded essays
- Total sentences
- Total grammar errors
- Error rate
- Average confidence score
- Analytics dashboard data

---

# 17. Train NLP Model with Lang-8 Dataset

## Dataset

Lang-8 Learner Corpus.

Example format:

```text
Incorrect sentence
Correct sentence
```

---

## Training Command

```bash
python app/services/trainer.py
```

Trained models will be saved in:

```text
models/
```

---

# 18. Test APIs with Postman

Import:

```text
English Essay Error Detection API.postman_collection.json
```

---

# 19. Check PostgreSQL Data

## Documents

```sql
SELECT * FROM documents;
```

---

## Sentences

```sql
SELECT * FROM sentences;
```

---

## Predictions

```sql
SELECT * FROM predictions;
```

---

# 20. Restart Server After Code Changes

After modifying models or routes:

```bash
CTRL + C
```

Then restart:

```bash
uvicorn app.main:app --reload
```

---

# 21. Common Errors

## ModuleNotFoundError

Check:

```text
__init__.py
```

---

## UndefinedColumn

Database schema is outdated.

Run:

```sql
ALTER TABLE ...
```

or recreate the database.

---

## invalid keyword argument

Missing field in SQLAlchemy model.

Example:

```python
file_type = Column(String(100))
```

---

# 22. Conclusion

This system provides:

- Automatic English essay analysis
- AI-based grammar error detection
- Student and document management
- NLP analytics and reporting
- Modern REST API architecture with FastAPI

This project is suitable for:

- NLP research projects
- Grammar Error Correction systems
- Educational analytics systems
- AI-assisted English learning applications
- Graduate thesis projects

