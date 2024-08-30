from fastapi import APIRouter


router = APIRouter()


@router.get("/time")
async def get_time():
    pass
