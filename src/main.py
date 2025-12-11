"""Minimal FastAPI app to be extended in later steps."""
from fastapi import FastAPI

app = FastAPI(title="Agentic PM Prototype API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Agentic PM prototype running"}
