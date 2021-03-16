# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def damage_to_amount(damages):
  converted_damages = []
  for damage in damages:
    if damage == "Damages not recorded":
      converted_damages.append(damage)
    else:
      num = float(damage[:-1])*conversion.get(damage[-1])
      converted_damages.append(num)
  return converted_damages

# test function by updating damages
updated_damages = damage_to_amount(damages)
print(updated_damages)
print(len(updated_damages))

# 2 
# Create a Table
table = []
for index in range(len(names)): 
   table.append({"Name": names[index],
   "Month": months[index],
   "Year": years[index],
   "Max Sustained Wind": max_sustained_winds[index],
   "Areas Affected": areas_affected[index],
   "Damage": updated_damages[index],
   "Deaths": deaths[index]})
print(table)
print(len(table))
# Create and view the hurricanes dictionary
def create_hurricanes_dict(k_list,v_dict):
  return dict(zip(k_list, v_dict))

hurricanes_dict = create_hurricanes_dict(names, table)
print("The hurricanes dictionary is: ", hurricanes_dict)

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
hurricanes_dict_year = create_hurricanes_dict(years, table)
print("\n The hurricanes dictionary organised by year is: ", hurricanes_dict_year)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def count_areas(dict_values): 
  new_dict = {}
  for hurricane in dict_values.values():
    for area in hurricane["Areas Affected"]:
      if area not in new_dict.keys():
        new_dict[area] = 1
      else:
        new_dict[area] += 1
  return new_dict

affected_areas_count = count_areas(hurricanes_dict)
print(affected_areas_count)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in

def find_most_affected_area(dic):
  max_area = 'Venezuela'
  max_area_count = 0
  for k, v in dic.items():
    if max_area_count < v:
      max_area = k
      max_area_count = v
  print("The most affected area is {} with {} hurricanes in the past".format(max_area, max_area_count))

most_affectd_area = find_most_affected_area(affected_areas_count)


# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def most_death_hurricane(dicti):
  max_name = 'Matthew'
  max_death_count = 0
  for k, v in dicti.items():
    #print(type(v["Deaths"]))
    if max_death_count < (v["Deaths"]):
      max_name = k
      max_death_count = (v["Deaths"])

  print("The most dangerous hurricane is {} with {} deaths in the past".format(max_name, max_death_count))

most_deaths_hurricane = most_death_hurricane(hurricanes_dict)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
for hurricane in hurricanes_dict.values():
    if 0 < hurricane["Deaths"] <= 100:
      hurricanes_by_mortality[1].append(hurricane["Name"])
    elif 100 < hurricane["Deaths"] <= 500:
      hurricanes_by_mortality[2].append(hurricane["Name"])
    elif 500 < hurricane["Deaths"] <= 1000:
      hurricanes_by_mortality[3].append(hurricane["Name"])
    elif 1000 < hurricane["Deaths"] <= 10000:
      hurricanes_by_mortality[4].append(hurricane["Name"])

print(hurricanes_by_mortality)



# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def most_damage_hurricane(dicti):
  max_name = 'Matthew'
  max_damage_count = 0
  for k, v in hurricanes_dict.items():
    if v["Damage"] != "Damages not recorded": 
      if max_damage_count < (v["Damage"]):
        max_name = k
        max_damage_count = (v["Damage"])

  print("The most expensive cost hurricane is {} with {} amount of damage cost in the past".format(max_name, max_damage_count))

most_cost_hurricane = most_damage_hurricane(hurricanes_dict)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

hurricanes_by_severity = {0:[],1:[],2:[],3:[],4:[],5:[]}
for hurricane in hurricanes_dict.values():
  if hurricane["Damage"] != "Damages not recorded": 
    if 0 < hurricane["Damage"] <= 100000000:
      hurricanes_by_severity[1].append(hurricane["Name"])
    elif 100 < hurricane["Damage"] <= 1000000000:
      hurricanes_by_severity[2].append(hurricane["Name"])
    elif 500 < hurricane["Damage"] <= 10000000000:
      hurricanes_by_severity[3].append(hurricane["Name"])
    elif 1000 < hurricane["Damage"] <= 50000000000:
      hurricanes_by_severity[4].append(hurricane["Name"])

print(hurricanes_by_severity)
