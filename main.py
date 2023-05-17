from fastapi import FastAPI
from routers.wellknown import wellknown
import json

app = FastAPI()
app.include_router(wellknown)
