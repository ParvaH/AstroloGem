# api/main.py
from fastapi import FastAPI
from api.schemas import ChartInput
from rag.generator import generate_response

app = FastAPI(title="AstroloGem API")


@app.get("/")
def root():
    return {"message": "Welcome to AstroloGem API", "docs": "/docs"}


@app.post("/analyze-chart")
def analyze_chart(data: ChartInput):
    return generate_response(data, endpoint="/analyze-chart")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"service": "AstroloGem", "version": "v2"}
