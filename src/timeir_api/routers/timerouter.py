from fastapi import APIRouter
from timeir_api.services.timeir_service import date_parser

router = APIRouter()


@router.get("/time")
async def get_time():
    dt = await date_parser()
    return {"time": dt}
