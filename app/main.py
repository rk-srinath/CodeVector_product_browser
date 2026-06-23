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
    category: str | None = Query(default=None)
):

    db = SessionLocal()

    query = db.query(Product)

    if category:
        query = query.filter(
            Product.category == category
        )

    products = (
        query
        .order_by(desc(Product.created_at))
        .limit(20)
        .all()
    )

    db.close()

    return products