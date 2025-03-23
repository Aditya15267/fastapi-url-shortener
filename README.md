# Fast API URL Shortener

A simple URL shortner build with FastAPI

## Features

- Shorten long URLs
- Redirect shorten URLs
- Fast and lightweight with FastAPI

## Installation

1. Clone repository:
   ```sh
   git clone https://github.com/Aditya15267/fastapi-url-shortener.git

2. Run the app:
   ```sh
   python -m uvicorn url_shortener:app --reload

3. Open in your browser: http://127.0.0.1:8000

## API Endpoints


| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST | /shorten_url | Shorten a URL |
| GET | /expand/{short_code} | Redirect to original URL |