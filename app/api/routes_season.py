from fastapi import APIRouter, HTTPException
from app.services.season_service import get_season_by_month, get_all_seasons
from app.common.exceptions.season_expcetions import SeasonNotFoundError, InvalidMonthError

router = APIRouter(prefix="/seasons", tags=["Season"])

@router.get("/")
async def all_seasons():
    try:
        return get_all_seasons()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{month}")
async def season_by_month(month: int):
    try:
      return get_season_by_month(month)
    except InvalidMonthError as e:
        raise HTTPException(status_code=400, detail=e.message)
    except SeasonNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")