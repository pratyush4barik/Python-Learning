# DAY - 9 
#Lists + Loops - Real-World Practice
#Favourite Movies Task
list_of_movies = []
count = 0
for i in range(5):
    movie = input(f"Enter the name of the movie - {i + 1} : ")
    movie = movie.upper()
    list_of_movies.append(movie)
    if movie[0] == 'T':
        count += 1
    else:
        continue
print(f"Your favourite movies are : {list_of_movies}")
print(f"Number of movies starting with 'T' : {count}")
#Word Filter Task
fruits_longer_than_five = []
fruits = ["apple", "banana", "cherry", "avocado", "grapes"]
for fruit in fruits:
    if fruit[0] is 'a':
        print(fruit, end=" ")
    else:
        pass
    if len(fruit) > 5:
        fruits_longer_than_five.append(fruit)
print(f"\nFruits longer than five characters: {fruits_longer_than_five}")
#Bonus Challenge
for i in range(3):
    name = input(f"\nEnter the name of person {i + 1} : ")
    print("Intials : ", end="")
    for j in name:
        if j.isupper():
            print(j, end=".")
        else:
            continue

        




