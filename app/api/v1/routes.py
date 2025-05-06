from fastapi import APIRouter
from app.services.products import get_products, get_all, get_product_by_type
from app.data.seasons import SEASONS
from app.data.regions import REGIONS
from app.data.tipos import TIPOS

router = APIRouter()

@router.get("/productos")
async def get_all_products():
    return get_all()

@router.get("/productos/{region}/{mes}")
async def productos(region: str, mes: str):
    return get_products(region, mes)

@router.get("/seasons")
async def get_seasons():
    return SEASONS

@router.get("/regions")
async def get_regions():
    return REGIONS

@router.get("/tipos")
async def get_tipos():
    return TIPOS

@router.get("/filter/{tipo}")
async def filter_by_type(tipo: str):
    return get_product_by_type(tipo)