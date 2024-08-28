
# autoagi.py
# Main file for the AutoAGI program

import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return "<h1>Welcome to AutoAGI</h1>"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
