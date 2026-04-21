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
# Purpose Statement: Take in a RegionCondition and compute the amount of CO2-equivalent emissions per person in the region per year, 
# returning 0.0 if the population is zero.
#3.1
def emissions_per_capita(rc: RegionCondition) -> float:
  if rc.pop == 0:
    return 0.0
  return (rc.ghg_rate / rc.pop)

#Task 3.2
# Purpose Statement: Take in a GlobeRect representing a region on Earth and compute the estimated surface area of the region 
# in square kilometers using a spherical Earth model.
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

#Tasl 3.3
# Purpose Statement: Take in a RegionCondition and compute the amount of CO2-equivalent emissions per square kilometer of the region,
#returning 0.0 if the region’s area is zero.
def emissions_per_square_kilometer(rc: RegionCondition) -> float:
  a = area(rc.region.rect)
  if a == 0:
    return 0.0
  return (rc.ghg_rate / a)

#Task 3.4
# Purpose Statement: Take in a list of RegionCondition values and return the name of the region with the highest population density
# (population divided by area) using recursion.
def densest_helper(rc_list: list[RegionCondition], i: int = 0) -> list[RegionCondition]:
  if i == len(rc_list) - 1:
    return rc_list[i]
  best_temp = densest_helper(rc_list, i + 1)
  current = rc_list[i]

  current_area = area(current.region.rect)
  temp_area = area(best_temp.region.rect)

  if current_area == 0:
    current_density = 0.0
  else:
    current_density = current.pop / current_area

  if temp_area == 0:
    temp_density = 0.0
  else:
    temp_density = temp.pop / temp_area

  if current_area >= temp_density:
    return current
  else: 
    return best_temp
 
def densest(rc_list: list[RegionCondition]) -> str:
    return densest_helper(rc_list).region.name

#Task 4
# Purpose Statement: Take in a RegionCondition and a number of years and compute a new RegionCondition representing 
# the projected state after applying terrain-based population growth and proportional emissions scaling over time.
def project_condition(rc: RegionCondition, years: int) -> RegionCondition:
    
    if rc.region.terrain == "ocean":
        rate = 0.0001
    elif rc.region.terrain == "mountains":
        rate = 0.0005
    elif rc.region.terrain == "forest":
        rate = -0.00001
    else:
        rate = 0.0003
    new_pop = rc.pop
    for _ in range(years):
        new_pop = new_pop * (1 + rate)
    if rc.pop == 0:
        new_ghg = 0.0
    else:
        new_ghg = rc.ghg_rate * (new_pop / rc.pop)
    return RegionCondition(rc.region, rc.year + years, int(new_pop), new_ghg)
  
  
  
  








