from pydantic_settings import BaseSettings


class MetadataSettings(BaseSettings):
    title: str = "TimeirAPI"
    summary: str | None = (
        "Access current dates in multiple calendars and get daily quotes, all extracted from time.ir. ⏰🚀"
    )
    description: str = """
### Access current dates in multiple calendars and get daily quotes, all extracted from time.ir.

You will be able to:

* **See dates in solar, lunar and Gregorian formats**.🎉
* **Get a random quote**.📣
"""
    version: str = "0.1.0"


def get_metadata_settings():
    return MetadataSettings()
