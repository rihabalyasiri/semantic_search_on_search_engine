import json
from filtering import filtering

filename = 'data/all_data_mai.json'

german_data = []

with open(filename, 'r') as file:
        try:
            data = json.load(file)
            german_data = filtering(data)
           
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
   


with open(f"data/german_all_data_mai.json", 'w') as file:
    json.dump(german_data, file, indent=4)