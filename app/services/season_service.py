from typing import List
from app.common.exceptions.season_expcetions import SeasonNotFoundError, InvalidMonthError
from app.data.seasons import SEASONS, MONTHS
from app.models.dto.seasonDto import SEASONSDTO

def get_all_seasons() -> List[dict]:
  return SEASONSDTO

def get_season_by_month(month: int) -> dict:
    if month < 1 or month > 13:
        raise InvalidMonthError(f"Invalid month: {month}")
    if month == 13:
        return {
            "season": MONTHS[13],
            "start_month": MONTHS[1],
            "end_month": MONTHS[12]
        }
    for season, start_month, end_month in SEASONS:
        if (start_month <= month <= end_month) or (start_month > end_month and (month >= start_month or month <= end_month)):
            return {
                "season": season,
                "start_month": MONTHS[start_month],
                "end_month": MONTHS[end_month]
            }
    raise SeasonNotFoundError(f"Season not found for month: {month}")