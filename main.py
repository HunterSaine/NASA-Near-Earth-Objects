import json
import requests

response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY')

json_data = response.json() if response and response.status_code == 200 else None
formatted_json = json.dumps(json_data, indent=2) #format json response
near_earth_objects = json_data["near_earth_objects"] #isoloate list of near earth objects
i = 0
while i < len(near_earth_objects): #iterate through list of near earth ojects and gather names of each neo
    neo = near_earth_objects[i]
    print(neo["name"])
    i += 1
    
neo = near_earth_objects[0]
file = open("data.txt", "w")
file.write(formatted_json)
file.close()
#print(neo["name"])