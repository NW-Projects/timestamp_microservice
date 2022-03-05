from fastapi import FastAPI, APIRouter
from datetime import datetime

 
router = APIRouter()

@router.get("/api")
def get_unix_timestamp():
    pass