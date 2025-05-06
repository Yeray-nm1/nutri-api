from fastapi import FastAPI
from app.api import routes_product, routes_season, routes_region

app = FastAPI(
    title="Nutri API",
    description="Devuelve productos de temporada según región y temporada",
    version="1.0.0"
)

app.include_router(routes_product.router, prefix="/api")
app.include_router(routes_season.router, prefix="/api")
app.include_router(routes_region.router, prefix="/api")