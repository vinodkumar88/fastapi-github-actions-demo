from fastapi import FastAPI
import os

app = FastAPI(title="FastAPI Pipeline Demo")

ENV = os.getenv("APP_ENV", "local")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!", "env": ENV}

@app.get("/health")
def health():
    return {"status": "ok", "env": ENV}
