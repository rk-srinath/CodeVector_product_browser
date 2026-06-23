# app/models.py

from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import Text
from sqlalchemy import Numeric
from sqlalchemy import TIMESTAMP

from app.database import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    category = Column(Text, nullable=False)
    price = Column(Numeric(10,2))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)