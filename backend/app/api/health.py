from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health")
def check_up():
    return JSONResponse(
        status_code=200,
        content={"status": "ok"}
    )


@router.get("/error")
def error():
    raise HTTPException(
        status_code=404,
        detail="error endpoint"
    )
