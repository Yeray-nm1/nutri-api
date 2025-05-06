from fastapi import FastAPI
from app.api.v1.routes import router as api_router

app = FastAPI(
    title="Nutri API",
    description="Devuelve productos de temporada según región y temporada",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")