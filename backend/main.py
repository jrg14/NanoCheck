from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI

from backend.core.config import Settings


app = FastAPI()

@lru_cache
def get_settings() -> Settings:
    return Settings()


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, str]:
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
    }