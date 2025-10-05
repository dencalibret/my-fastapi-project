from fastapi import FastAPI
from src.core import router as common_routes

app = FastAPI(
    title="Lab3 FastAPI Project",
    description="Lab project with FastAPI and Swagger UI",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    servers=[
        {"url": "http://72.145.10.46:8000", "description": "Production server"},
        {"url": "http://localhost:8000", "description": "Development server"},
    ]
)

app.include_router(common_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Lab3 API"}
