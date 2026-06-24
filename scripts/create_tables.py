from app.database import Base, engine
from app.models import Product

Base.metadata.create_all(bind=engine)