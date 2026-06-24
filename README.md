# CodeVector Product Browser

A high-performance backend application built for the CodeVector Backend Internship Assignment.

The application allows users to browse a catalog of 200,000 products, filter products by category, and paginate through results efficiently using cursor-based pagination.

---

## Features

- Browse 200,000 products
- Category-based filtering
- Cursor-based pagination
- Fast PostgreSQL queries
- Bulk product generation script
- REST API using FastAPI
- Simple frontend UI (Bonus)
- Swagger API Documentation

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy

### Database
- PostgreSQL

### Data Generation
- Faker

### Frontend (Bonus)
- HTML
- CSS
- JavaScript

---

## Project Structure

```text
codevector-product-browser/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── scripts/
│   └── seed.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .env
├── requirements.txt
└── README.md
```

---

## Database Schema

### Products Table

| Column | Type |
|----------|----------|
| id | BIGSERIAL |
| name | TEXT |
| category | TEXT |
| price | NUMERIC |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## Why PostgreSQL?

PostgreSQL was chosen because it is a reliable, production-grade relational database that efficiently handles large datasets and supports indexing for high-performance queries.

---

## Product Generation

A seed script generates 200,000 products using Faker.

To improve insertion performance, products are inserted in batches using SQLAlchemy's bulk insert functionality instead of inserting records one by one.

Run:

```bash
python -m scripts.seed
```

---

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "CodeVector API Running"
}
```

---

### Get Products

```http
GET /products
```

Returns the latest products.

---

### Category Filter

```http
GET /products?category=Books
```

Returns products belonging to the specified category.

---

### Cursor Pagination

```http
GET /products?cursor=199996&limit=20
```

Returns products with IDs lower than the provided cursor value.

---

## Why Cursor Pagination?

Cursor pagination was chosen instead of OFFSET pagination because:

- Faster on large datasets
- Scales better
- Avoids duplicate records
- Prevents missing records when new products are inserted while users are browsing

Example:

```http
GET /products?cursor=199996&limit=20
```

---

## Database Indexing

Indexes were added to improve query performance.

```sql
CREATE INDEX idx_products_category
ON products(category);
```

Benefits:

- Faster category filtering
- Reduced database scan time
- Better scalability

---

## Running Locally

### Clone Repository

```bash
git clone <repo-url>
cd codevector-product-browser
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/codevector_db
```

### Start API

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend

A simple frontend was created to demonstrate:

- Product browsing
- Category filtering
- Cursor-based pagination

The assignment primarily focuses on backend development, so frontend functionality was intentionally kept minimal.

---

## Future Improvements

With more time, I would add:

- Authentication & Authorization
- Redis Caching
- Automated Testing
- Docker Support
- CI/CD Pipeline
- Advanced Cursor Pagination using `(updated_at, id)`
- Search Functionality

---

## How I Used AI

I used AI tools (ChatGPT) to:

- Understand cursor pagination
- Learn PostgreSQL indexing concepts
- Debug development issues
- Accelerate implementation

All generated code was reviewed, tested, understood, and modified before being included in the final solution.

---
