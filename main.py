from fastapi import FastAPI
from routers.wellknown import wellknown
import json

app = FastAPI(title="Product Search", version="1.0")
app.include_router(wellknown)
