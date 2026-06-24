from fastapi import FastAPI, Query
from sqlalchemy import desc

from app.database import SessionLocal
from app.models import Product
from app.schemas import ProductResponse

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "CodeVector API Running"
    }


@app.get(
    "/products",
    response_model=list[ProductResponse]
)
def get_products(
    category: str | None = None,
    cursor: int | None = None,
    limit: int = 20
):

    db = SessionLocal()

    query = db.query(Product)

    if category:
        query = query.filter(
            Product.category == category
        )

    if cursor:
        query = query.filter(
            Product.id < cursor
        )

    products = (
        query
        .order_by(desc(Product.id))
        .limit(limit)
        .all()
    )

    db.close()

    return products