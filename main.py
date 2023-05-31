#@S
from fastapi import FastAPI
from routers.wellknown import wellknown
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.include_router(wellknown)
app.add_middleware(CORSMiddleware, allow_origins=["https://chat.openai.com"])

with open("./data/products.json", "r") as f:
    products = json.load(f)


@app.get("/products", summary="Get a list of products", operation_id="getProducts")
async def get_products(query: str = None):
    """
    Returns a list of products, optionally filtered by providing a query parameter.
    """
    if query:
        keywords = query.lower().split()
        return [
            product
            for product in products
            if all(keyword in str(product.values()).lower() for keyword in keywords)
        ]
    return products
