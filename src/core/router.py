from fastapi import APIRouter
import datetime

router = APIRouter(prefix="/common", tags=["common"])

@router.get(
    "/healthcheck",
    summary="Health check endpoint",
    description="Returns the health status of the service",
    response_description="Service status and message"
)
def healthcheck():
    return {"status": "ok", "message": "Service is running"}

@router.get(
    "/time",
    summary="Get server time",
    description="Returns the current server time in ISO format",
    response_description="Current server time"
)
def get_time():
    return {"server_time": datetime.datetime.now().isoformat()}
