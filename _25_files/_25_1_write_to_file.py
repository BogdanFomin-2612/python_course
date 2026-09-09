import json

data = {"name": "Mike", "age": 20, "city": "Gdansk"}
file = open("_25_files/files/data.json", "w")     #? "w" - означает WRIGHT, то есть запись в файл
# json.dump(data, file, indent = 4)                 #? indent = 4 - означает отступы между строк (просто для красоты)
# file.close()

