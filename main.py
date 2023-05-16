from fastapi import FastAPI
from routers.wellknown import wellknown
import json

app = FastAPI()
app.include_router(wellknown)

# load products from data
with open('data/products.json') as f:
    products = json.load(f)

# /products?query=list-of-keywords
@app.get("/products")
async def get_products(query: str = None):
    if query:
        query = query.lower()
        return [product for product in products if query in product['description'].lower()]
    return products