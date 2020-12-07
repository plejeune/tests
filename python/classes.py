# Create a class 1
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)


# Create a class 2
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Add a passenger
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # How many seats max
    def open_seats(self):
        return self.capacity - len(self.passengers)

# Define the capacity into a new variable
flight = Flight(3)

# Define new people to add
people = ["Harry", "Ron", "Hermione", "Ginny"]

# Sort people (for testing)
people.sort()

# Display success or not
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seat for {person}.")