#Task 1
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

#Task 2
#Denver, United States
denver_rect = GlobeRect(39.4, 40.1, -105.3, -104.5)
denver_region = Region(denver_rect, "Denver", "other")
denver_condition = RegionCondition(denver_region, 2020, 3000000, 100000000.0)
#Santiago, Chile
santiago_rect = GlobeRect(-33.8, -33.2, -70.9, -70.3)
santiago_region = Region(santiago_rect, "Santiago", "other")
santiago_condition = RegionCondition(santiago_region, 2020, 6000000, 80000000.0)
#Pacific Ocean
pacific_rect = GlobeRect(10.0, 20.0, -160.0, -140.0)
pacific_region = Region(pacific_rect, "Central Pacific", "ocean")
pacific_condition = RegionCondition(pacific_region, 2020, 0, 0.0)
#SLO 
slo_rect = GlobeRect(35.0, 35.5, -121.2, -120.2)
slo_region = Region(slo_rect, "San Luis Obispo Area", "other")
slo_condition = RegionCondition(slo_region, 2020, 280000, 1000000.0)

region_conditions = [denver_condition, santiago_condition, pacific_condition, slo_condition]

#Task 3
#3.1
def emissions_per_capita(rc: RegionCondition) -> float:
  if rc.pop == 0:
    return 0.0
  return (rc.ghg_rate / rc.pop)

#Task 3.2
def area(gr: GlobeRect) -> float:
  R = 6378.1
    lo_lat = math.radians(gr.lo_lat)
    hi_lat = math.radians(gr.hi_lat)
    west = math.radians(gr.west_long)
    east = math.radians(gr.east_long)

    diff = east - west
    if diff < 0:
        diff += 2 * math.pi

    return (R ** 2) * abs(diff) * abs(math.sin(hi_lat) - math.sin(lo_lat))







