import os
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

COLOSSYAN_API_KEY = os.getenv("COLOSSYAN_API_KEY")

@app.get("/api/actors")
def list_actors():
    headers = {
        "Authorization": f"Bearer {COLOSSYAN_API_KEY}"
    }
    try:
        response = requests.get("https://api.colossyan.com/v1/assets/actors", headers=headers)
        response.raise_for_status()
        data = response.json()
        avatars = [
            {
                "id": actor.get("name"),
                "displayName": actor.get("displayName"),
                "type": actor.get("type"),
                "language": actor.get("language")
            } for actor in data
        ]
        return JSONResponse(content={"avatars": avatars})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})