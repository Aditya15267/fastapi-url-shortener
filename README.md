# Fast API URL Shortener

A simple and fast URL shortner build using **FastAPI** for the backend and **HTML + Tailwind CSS + JavaScript** for the frontend.

## Features

- Shorten long URLs with a single click
- Expand shortened URLs back to original
- Fast and lightweight FastAPI backend
- Clean and modern UI using Tailwind CSS
- Handles input validation and basic error messaging

## Installation
Install the required dependency:
```sh
   pip install fastapi uvicorn
```

## How to use

1. Clone repository:
   ```sh
   git clone https://github.com/Aditya15267/fastapi-url-shortener.git
2. Run the backend server:
   ```sh
   python -m uvicorn url_shortener:app --reload
   ```
   Your FastAPI server will be running on:

   ```http://127.0.0.1:8000```
3. Simply open ```index.html``` in your browser (double click or use Live Server if using VS Code). Make sure your FastAPI server is running before interacting.

## API Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST | /shorten_url | Shorten a URL |
| GET | /expand/{short_code} | Redirect to original URL |

## Example

### Request:

```json
POST /shorten_url
{
   "long_url": "https://www.example.com/long/url/path"
}
```

### Response:

```json
{
  "short_url": "http://short.ly/TMBPwN"
}
```

## Tech Stack

- **Backend**: FastAPI, Python
- **Frontend**: HTML, Tailwind CSS, Vanilla JS
- **Othes**: CORS Middleware for API access