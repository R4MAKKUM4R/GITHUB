import json

with open("data.json","r") as f:
 loaded_data=json.load(f)
    
 print(loaded_data)