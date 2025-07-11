# DAY - 6
animals = ("Dog", "Cat", "Elephant", "Lion", "Tiger")
#printing the first and last element of the tuple
print(f"First element: {animals[0]}")
print(f"Last element: {animals[-1]}")
# printing the whole tuple using loop
for animal in animals:
    print(animal, end=" ")
# sets
set = {1, 2, 2, 3, 4, 4}
print(f"\nset : {set}")
#creating two sets 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Union of set1 and set2: {set1 | set2}")  # Union of two sets
