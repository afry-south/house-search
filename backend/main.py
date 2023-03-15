from fastapi import FastAPI
from booli import booli

app = FastAPI(title="House Search")
app.include_router(booli.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

