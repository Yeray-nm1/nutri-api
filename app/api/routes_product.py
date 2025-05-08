from fastapi import APIRouter, HTTPException
from app.services.product_service import get_products, get_all, get_product_by_id, get_products_by_type
from app.common.exceptions.product_exceptions import ProductNotFoundError, InvalidProductInputError

router = APIRouter(prefix="/products", tags=["Productos"])

@router.get("/")
async def get_all_products():
    try:
        return get_all()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{id:int}")
async def product_by_id(id: int):
    try:
        return get_product_by_id(id)
    except InvalidProductInputError as e:
        raise HTTPException(status_code=400, detail=e.message)
    except ProductNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{region}/{mes}")
async def productos(region: str, mes: str):
    return get_products(region, mes)

@router.get("/{tipo:str}")
async def products_by_type(tipo: str):
    return get_products_by_type(tipo)