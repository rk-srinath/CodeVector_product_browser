from sqlalchemy import Column, BigInteger, Text, Numeric, TIMESTAMP
from app.database import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    name = Column(Text, nullable=False)
    category = Column(Text, nullable=False)
    price = Column(Numeric(10, 2))

    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)