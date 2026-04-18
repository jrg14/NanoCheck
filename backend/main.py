from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI

from backend.core.config import Settings
from backend.core.db import create_tables
from backend.modules.users import router as users_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@lru_cache
def get_settings() -> Settings:
    return Settings()


@app.on_startup()
def on_startup() -> None:
    create_tables()


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, str]:
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
    }


app.include_router(users_router)
