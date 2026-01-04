from fastapi import FastAPI

import app.models
from app.routers.transaction import router as tx_router

app = FastAPI(title="Family Expense API")
app.include_router(tx_router)


@app.get("/")
def health():
    return {"status": "ok"}
