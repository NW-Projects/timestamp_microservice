from fastapi import FastAPI
from datetime import datetime
from time import time
from src import routes


app = FastAPI()

app.include_router(routes.router)

@app.get("/")
async def root():
    return {"Unix": time(), "Now": datetime.now().strftime('%d-%m-%Y Time:%H:%M:%S')}