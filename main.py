import json
import requests

response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY')

json_data = response.json() if response and response.status_code == 200 else None
#print(json_data)
print()
print()
print()
close_objects = json_data["near_earth_objects"]
print("Print each key-value pair from JSON response")
i = 0
for key, value in close_objects.items():
    print(key, ":", value)
    print()



#file = open("data.txt", "a")
#file.write(json_data)
#file.close()