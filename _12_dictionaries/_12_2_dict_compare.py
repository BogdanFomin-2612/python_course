person = {
    "name": "John",
    "age": 20,
    "city": "New York"
}

other_person = {
    "city": "New York",
    "name": "John",
    "age": 20
}

next_person = {
    "name": "Bogdan",
    "age": 20,
    "city": "Gdańsk",
    "country": "Poland"
}

# print(person == other_person)
# print(person == next_person)

#? Неудобное присвоение значений
#! other_person.update(next_person)
#! print(other_person)

#? Удобное присвоение значений
#* other_person = other_person | next_person
#* print(other_person)