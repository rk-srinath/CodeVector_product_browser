from fastapi import FastAPI
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
def get_products():

    db = SessionLocal()

    products = (
        db.query(Product)
        .order_by(desc(Product.created_at))
        .limit(20)
        .all()
    )

    db.close()

    return products