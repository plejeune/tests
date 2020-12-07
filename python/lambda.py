# Create a dictionary inside a list
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# Sort by type - version1
def f(person):
    return person["name"]
def h(person):
    return person["house"]
people.sort(key=h)


# Sort by type - version2
people.sort(key=lambda person: person["name"])
people.sort(key=lambda person: person["house"])

# Print people
print(people)