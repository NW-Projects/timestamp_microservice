from time import strftime
from fastapi import FastAPI, APIRouter, HTTPException, Query
from datetime import datetime
from dateutil.parser import parse


 
router = APIRouter()

@router.get("/api/{ut}")
def unix_to_datetime(ut: float):
    d = datetime.utcfromtimestamp(ut)
    return {"Unix": ut, "UTC time": d.strftime("%a, %d %b %Y %H:%M:%S GMT")}



@router.get("/{date}")
def datetime_to_unix(date: str ):
   
    unix_timestamp = datetime.strptime(date, "%Y-%m-%d" ).timestamp()   
    utc_time = datetime.utcfromtimestamp(unix_timestamp).strftime("%a, %d %b %Y %H:%M:%S GMT")

    return {"Unix Timestamp" : unix_timestamp, "UTC Time": utc_time}


