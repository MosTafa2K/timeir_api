from fastapi import APIRouter
from timeir_api.services.timeir_service import get_current_date, get_random_quote

router = APIRouter()


@router.get("/time")
async def current_date():
    now = await get_current_date()
    return {"date": now}


@router.get("/quote")
async def random_quote():
    quote = await get_random_quote()
    return {"Quote": quote}
