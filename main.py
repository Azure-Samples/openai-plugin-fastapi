from fastapi import FastAPI
from routers.wellknown import wellknown
from fastapi.middleware.cors import CORSMiddleware

import json

app = FastAPI()
app.include_router(wellknown)
app.add_middleware(CORSMiddleware, allow_origins=["https://chat.openai.com"])

# Load fake products from product.json
with open("./data/products.json", "r") as f:
    products = json.load(f)


@app.get("/products")
async def get_products(query: str = None):
    """Get products from the fake database"""
    if query:
        return [
            product for product in products if query.lower() in product["description"]
        ]
    return products
