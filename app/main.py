from fastapi import FastAPI

import app.models
from app.routers.account import router as account_router
from app.routers.category import router as cat_router
from app.routers.family import router as family_router
from app.routers.transaction import router as tx_router

app = FastAPI(title="Expense API")

app.include_router(tx_router)
app.include_router(family_router)
app.include_router(cat_router)
app.include_router(account_router)


@app.get("/", tags=["Health"])
def health():
    return {"status": "ok"}
