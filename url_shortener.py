from fastapi import FastAPI
from pydantic import BaseModel
import random
import string
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fake db to store the urls
url_db = {}
BASE_URL = "http://short.ly/"

class UrlShorten(BaseModel):
    long_url: str

# Function to generate short code
def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# API to shorten the url
@app.post("/shorten_url")
def shorten_url(request: UrlShorten):
    short_code = generate_short_code()
    url_db[short_code] = request.long_url
    return {"short_url": BASE_URL + short_code}

# API to retrieve the original url
@app.get("/expand/{short_code}")
def get_original_url(short_code: str):
    long_url = url_db.get(short_code)
    if not long_url:
        return {"error": "Short code not found"}
    return {"long_url": long_url}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)