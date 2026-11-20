import json

user_data = {
    "name":"Alex",
    "age": 28,
    "is_active": True,
    "skills":["Python", "HTML", "SQL"],
}

file_name = "data.json"

file = open(file_name, "w")

json.dump(user_data, file, indent=4)

file.close()

print("Data successfully written!")