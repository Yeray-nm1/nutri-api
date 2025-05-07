from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_product, routes_season, routes_region

app = FastAPI(
    title="Nutri API",
    description="Devuelve productos de temporada según región y temporada",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routes_product.router, prefix="/api")
app.include_router(routes_season.router, prefix="/api")
app.include_router(routes_region.router, prefix="/api")