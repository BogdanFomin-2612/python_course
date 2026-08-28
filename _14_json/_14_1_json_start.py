import json

book = {
    'title': "1984",
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'dawdawd980980-98080980awdawd-09aw8d098aw09d80-awdd988dw898',
    'count': 30,
    'genres': ['dystopia']
}
json_string = json.dumps(book)
print(type(json_string))
print(json_string)

# json_string = '{"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "dawdawd980980-98080980awdawd-09aw8d098aw09d80-awdd988dw898"}'

# book = json.loads(json_string)
# print(type(book))
# print(book)

