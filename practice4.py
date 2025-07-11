# DAY - 5
# List methods i should know : appened, insert, remove, pop, len, sort, reverse, count, index
#problem no - 1
my_list = ["Apple", "Bannana", "Watermelon", "Orange", "Grapes"]
#printing the first and last element of the list
print(f"First elemeny : {my_list[0]}")
print(f"Last element : {my_list[-1]}")
my_list.append("Pineapple")  # Adding an element to the end of the list
my_list.remove("Apple")# Removing an element from the list
#problem no - 2
list = []
for i in range(1,3):
    num = int(input(f"Enter the number {i} : "))
    list.append(num)  # Adding the number to the list
print(f"Numbers List : {list}")
