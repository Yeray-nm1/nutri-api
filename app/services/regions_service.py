from typing import List
from app.data.regions import REGIONS
from app.common.utils.normalize import normalize_text
from app.common.exceptions.region_exceptions import RegionNotFoundError

def get_all_regions() -> List[str]:
  return REGIONS

def get_region_by_name(region_name: str) -> str:
  normalized_region = normalize_text(region_name)
  for region in REGIONS:
    if normalize_text(region) == normalized_region:
      return region
  raise RegionNotFoundError(f"Region '{region_name}' not found")