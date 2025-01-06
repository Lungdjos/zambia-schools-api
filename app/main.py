from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Zambia Schools API",
    description="API for managing primary and secondary schools in Zambia",
    version="1.0.0",
    debug=True
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Zambia Schools API"}
