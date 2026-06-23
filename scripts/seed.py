from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import random
import os
from dotenv import load_dotenv

from app.models import Product

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

fake = Faker()

categories = [
    "Electronics",
    "Mobile",
    "Fashion",
    "Books",
    "Home",
    "Sports"
]

TOTAL_PRODUCTS = 200000
BATCH_SIZE = 5000

session = Session()

print("Generating products...")

for batch_start in range(0, TOTAL_PRODUCTS, BATCH_SIZE):

    products = []

    for _ in range(BATCH_SIZE):

        product = Product(
            name=fake.company(),
            category=random.choice(categories),
            price=random.randint(100, 100000),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        products.append(product)

    session.bulk_save_objects(products)
    session.commit()

    print(
        f"Inserted {batch_start + BATCH_SIZE}/{TOTAL_PRODUCTS}"
    )

session.close()

print("Done!")