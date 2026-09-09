import json

file = open("_25_files/files/data.json", "r")   #? "r" - read
loaded_data = json.load(file)
file.close()
print(loaded_data)