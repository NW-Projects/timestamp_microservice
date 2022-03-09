from fastapi import FastAPI
from datetime import datetime
from time import time
import re


app = FastAPI()


@app.get("/")
def root():
    return {"Unix": time(), "UTC time now": datetime.utcnow().isoformat()}


@app.get("/api/{input}")
def unix_datetime(input: str):
    try: 
        if re.search("-", input):
            unix_timestamp = datetime.strptime(input, "%Y-%m-%d" ).timestamp()   
            utc_time = datetime.utcfromtimestamp(unix_timestamp).strftime("%a, %d %b %Y %H:%M:%S GMT")

            return {"Unix Timestamp" : unix_timestamp, "UTC Time": utc_time}

        else:
            inp = float(input)
            utc = datetime.utcfromtimestamp(inp)
            return {"Unix": input, "UTC time": utc.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    except:
        return {"error": "Invalid Entry"}
