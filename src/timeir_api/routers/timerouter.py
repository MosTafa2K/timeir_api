from fastapi import APIRouter
from timeir_api.services.timeir_service import get_current_date

router = APIRouter()


@router.get("/time")
async def current_date():
    now = await get_current_date()
    return {"date": now}
