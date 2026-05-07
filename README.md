# README.md

# English Essay Error Detection System

Hệ thống backend FastAPI dùng để nhận diện lỗi sai trong bài luận tiếng Anh của học viên bằng mô hình Transformer/BERT được train từ Lang-8 Dataset.

---

# 1. Chức năng hệ thống

Hệ thống hỗ trợ:

* Upload file PDF.
* Parse nội dung PDF.
* Tách câu tự động.
* Lưu dữ liệu vào PostgreSQL.
* Detect lỗi ngữ pháp/chính tả.
* Sinh câu sửa lỗi.
* Train model từ Lang-8 dataset.
* Thống kê lỗi theo document/user.
* REST API bằng FastAPI.
* Docker deployment.

---

# 2. Công nghệ sử dụng

| Thành phần     | Công nghệ                |
| -------------- | ------------------------ |
| Backend        | FastAPI                  |
| Database       | PostgreSQL               |
| NLP Model      | HuggingFace Transformers |
| ML Framework   | PyTorch                  |
| PDF Parser     | PyPDF2                   |
| Sentence Split | NLTK                     |
| ORM            | SQLAlchemy               |
| API Docs       | Swagger                  |
| Container      | Docker                   |

---

# 3. Cấu trúc project

```bash
english-essay-gec/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   ├── ml/
│   └── main.py
│
├── data/
│   ├── lang8/
│   └── uploads/
│
├── sql/
│   └── schema.sql
│
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

# 4. Yêu cầu hệ thống

* Python >= 3.10
* PostgreSQL >= 14
* Docker Desktop
* Git

---

# 5. Clone source code

```bash
git clone https://github.com/your-repository/english-essay-gec.git

cd english-essay-gec
```

---

# 6. Tạo môi trường ảo

## Windows

```bash
python -m venv venv

venv\\Scripts\\activate
```

## Linux / MacOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 7. Cài dependencies

```bash
pip install -r requirements.txt
```

---

# 8. Chạy PostgreSQL bằng Docker

```bash
docker compose up -d
```

Kiểm tra container:

```bash
docker ps
```

---

# 9. Tạo database schema

Mở PostgreSQL và chạy:

```bash
sql/schema.sql
```

Hoặc:

```bash
psql -U postgres -d postgres -f sql/schema.sql
```

---

# 10. Tạo thư mục dataset

```bash
mkdir data/lang8
mkdir data/uploads
```

---

# 11. Thêm Lang-8 dataset

Copy file:

```bash
lang8.csv
```

vào:

```bash
data/lang8/
```

Dataset yêu cầu format:

| source        | target         |
| ------------- | -------------- |
| I goes school | I go to school |
| She have book | She has a book |

---

# 12. Train model

API train:

```bash
POST /train/lang8
```

Hoặc chạy trực tiếp:

```bash
python app/ml/train_bert_gec.py
```

Model sẽ lưu tại:

```bash
models_saved/bert-gec/
```

---

# 13. Chạy FastAPI server

```bash
uvicorn app.main:app --reload
```

Server chạy tại:

```bash
http://localhost:8000
```

---

# 14. Swagger API

Swagger UI:

```bash
http://localhost:8000/docs
```

Redoc:

```bash
http://localhost:8000/redoc
```

---

# 15. Workflow chạy hệ thống

## Bước 1

Khởi động PostgreSQL.

```bash
docker compose up -d
```

## Bước 2

Tạo schema database.

```bash
psql -U postgres -d postgres -f sql/schema.sql
```

## Bước 3

Train model Lang-8.

```bash
POST /train/lang8
```

## Bước 4

Chạy FastAPI.

```bash
uvicorn app.main:app --reload
```

## Bước 5

Upload PDF.

```bash
POST /documents/upload
```

## Bước 6

Detect lỗi.

```bash
POST /documents/{document_id}/detect
```

## Bước 7

Lấy danh sách lỗi.

```bash
GET /documents/{document_id}/errors
```

## Bước 8

Xem thống kê.

```bash
GET /statistics/user/{author_id}
```

---

# 16. Danh sách API

| API                     | Method | Chức năng          |
| ----------------------- | ------ | ------------------ |
| /                       | GET    | Kiểm tra server    |
| /documents/upload       | POST   | Upload PDF         |
| /documents/{id}/detect  | POST   | Detect lỗi         |
| /documents/{id}/errors  | GET    | Lấy toàn bộ lỗi    |
| /statistics/user/{id}   | GET    | Thống kê theo user |
| /statistics/errors/type | GET    | Thống kê loại lỗi  |
| /train/lang8            | POST   | Train model        |

---

# 17. Test API bằng Postman

Import file:

```bash
english_essay_api.postman_collection.json
```

Sau đó:

1. Upload PDF.
2. Copy document_id.
3. Detect errors.
4. Get errors.
5. Statistics.

---

# 18. Cấu hình database

File:

```python
app/core/database.py
```

Cấu hình mặc định:

```python
DATABASE_URL = "postgresql://postgres:root@localhost:5432/postgres"
```

---

# 19. Docker build

## Build image

```bash
docker build -t english-gec .
```

## Run container

```bash
docker run -p 8000:8000 english-gec
```

---

# 20. Một số lỗi thường gặp

## Lỗi thiếu punkt

```bash
LookupError: Resource punkt not found
```

Fix:

```python
import nltk
nltk.download('punkt')
```

---

## Lỗi PostgreSQL connection

Kiểm tra:

```bash
docker ps
```

Hoặc:

```bash
docker compose up -d
```

---

## Lỗi thiếu model

Train model trước:

```bash
POST /train/lang8
```

---

# 21. Định hướng mở rộng

* Neo4j Knowledge Graph.
* BART/T5/PhoBERT.
* Redis cache.
* Celery background jobs.
* OCR cho PDF scan.
* Dashboard ReactJS.
* Multi-language support.
* Real-time grammar correction.
* RAG + LLM integration.
