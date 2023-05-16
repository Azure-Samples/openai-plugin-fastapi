from fastapi import FastAPI
from routers.wellknown import wellknown
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
import json

app = FastAPI(title="Product Search", version="1.0")
app.include_router(wellknown)
app.add_middleware(CORSMiddleware, allow_origins=["https://chat.openai.com"])

with open("./data/products.json", "r") as f:
    products = json.load(f)

class Product(BaseModel):
    name: str
    description: str
    category: str
    size: str
    price: float

class ProductQuery(BaseModel):
    query: Optional[str] = None

@app.get("/products", response_model=List[Product], summary="Get a list of products", operation_id="getProducts")
async def get_products(query: Optional[str] = None):
    """
    Returns a list of products, optionally filtered by providing a query parameter.
    """
    if query:
        return [product for product in products if query.lower() in str(product.values()).lower()]
    return products
