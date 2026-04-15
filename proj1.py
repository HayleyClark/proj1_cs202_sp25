@dataclass(frozen=True)
class GlobeRect:
  lo_lat: float
  hi_lat: float
  west_long: float
  east_long: float

@dataclass(frozen=True)
class Region:
  rect: GlobalRect  #Physical boundaries
  name: str        #Name of region
  terrain: str     #Must be "ocean", "mountains", "forest", or "other"

@dataclass(frozen=True)
class RegionCondition:
  region: Region      
  year: int        #Year of observation
  pop: int         #Population in that year
  ghg_rate: float  #Greenhouse gas emission for that year
