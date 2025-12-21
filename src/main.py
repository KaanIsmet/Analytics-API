from fastapi import FastAPI
from routers import router

app = FastAPI(
    title="Stock Analytics API",
    description="API for stocks via yfinance",
    version="0.1.0"
)

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "OK"}