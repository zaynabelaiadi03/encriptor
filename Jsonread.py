import json

file_name = "data.json"

file = open(file_name, "r")

loaded_data = json.load(file)

file.close()

print(loaded_data)

