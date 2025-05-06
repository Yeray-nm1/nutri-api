from fastapi import APIRouter, HTTPException
from app.services.regions_service import get_region_by_name, get_all_regions
from app.common.exceptions.region_exceptions import RegionNotFoundError

router = APIRouter(prefix="/regions", tags=["Region"])

@router.get("/")
async def all_regions():
    try:
        return get_all_regions()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/{region_name}")
async def region_by_name(region_name: str):
    try:
        return get_region_by_name(region_name)
    except RegionNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")