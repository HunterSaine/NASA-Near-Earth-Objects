import json
import requests

response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=QmQmoDsAK7sFaJhXlHUy4BsGVHKZd0kCY73fgF29')

json_data = response.json() if response and response.status_code == 200 else None
formatted_json = json.dumps(json_data, indent=2) #format json response
near_earth_objects = json_data["near_earth_objects"] #isoloate list of near earth objects
i = 0
neo_id_list = []    
neo_name_list = []
neo_miss_distance = []

while i < len(near_earth_objects): #iterate through list of near earth ojects and gather names of each neo
    neo = near_earth_objects[i]
    #print(neo["id"])
    id = neo["id"]
    name = neo["name"]
    neo_id_list.append(neo["id"])  #add id's to list variable
    neo_name_list.append(neo["name"]) #add names to list variable
    diameter = None
    for d in neo["estimated_diameter"]:
        diameter = neo["estimated_diameter"]
        kilometers = diameter["kilometers"]
    print(f"NEO ID: {id} Name: {name} Estimated Diameter: Between {kilometers["estimated_diameter_min"]:.2f} and {kilometers["estimated_diameter_max"]:.2f} Kilometers")
    print()
    i += 1



#print(neo_id_list)
#print(neo_name_list)
#print(neo_miss_distance)
file = open("data.txt", "w")
file.write(formatted_json)
file.close()
