from fastapi import FastAPI

from timeir_api.routers import timerouter
from timeir_api.settings.metadata_config import get_metadata_settings


metadata = get_metadata_settings()
app = FastAPI(
    title=metadata.title,
    description=metadata.description,
    summary=metadata.summary,
    version=metadata.version,
)
app.include_router(timerouter.router, tags=["Timeir"], prefix="/api/v1")


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome To Unofficial Timeir API✨"}
