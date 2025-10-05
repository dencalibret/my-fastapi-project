from fastapi import FastAPI
from src.core import router as common_routes

app = FastAPI(
    title="Lab3 FastAPI Project",
    description="Lab project with FastAPI and Swagger UI",
    version="0.1.0"
)

app.include_router(common_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Lab3 API"}
