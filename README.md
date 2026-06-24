# CodeVector Product Browser

A backend application built using FastAPI and PostgreSQL that allows users to browse 200,000 products with category filtering and efficient cursor-based pagination.

## Features

* Browse 200,000 products
* Category-based filtering
* Cursor-based pagination
* Bulk product generation script
* PostgreSQL database
* FastAPI REST API
* Swagger API Documentation
* Simple frontend UI (Bonus)

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL (Neon)
* HTML, CSS, JavaScript

## API Endpoints

### Get Products

```http
GET /products
```

### Filter by Category

```http
GET /products?category=Books
```

### Cursor Pagination

```http
GET /products?cursor=199996&limit=20
```

## Design Decisions

### Why Cursor Pagination?

Cursor pagination was chosen instead of OFFSET pagination because it:

* Performs better on large datasets
* Prevents duplicate records
* Avoids missing records when new products are added during browsing

### Why PostgreSQL?

PostgreSQL provides reliable performance, indexing support, and scalability for handling large datasets efficiently.

## Running Locally

```bash
pip install -r requirements.txt

python -m scripts.create_tables

python -m scripts.seed

uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Deployment

### API

[https://your-render-url.onrender.com/](https://codevector-product-browser-slz4.onrender.com/)

### Swagger Docs

[https://your-render-url.onrender.com/](https://codevector-product-browser-slz4.onrender.com/docs)

### UI

[https://your-render-url.onrender.com/](https://codevector-product-browser-slz4.onrender.com/ui)

## AI Usage

AI tools were used for learning concepts, debugging issues, and accelerating implementation. All code was reviewed, understood, tested, and modified before submission.
