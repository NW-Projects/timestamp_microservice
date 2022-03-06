from fastapi import FastAPI
from datetime import datetime
from time import time
from routers import urls


app = FastAPI()

app.include_router(urls.router)

@app.get("/")
async def root():
    return {"Unix": time(), "UTC time now": datetime.utcnow().isoformat()}
