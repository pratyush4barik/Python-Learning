# DAY - 11
#Functions and Scope
# TASK - 1
def greet_user(name):
    return f"Hello, {name}!"
def add_numbers(a, b):
    return f"Sum : {a+b}"
def is_even(number):
    return f"Even : {number%2 == 0}"
name = input("Enter the name of the user : ")
print(greet_user(name)) 
num1 = int(input("Enter  numebr - 1 : "))
num2 = int(input("Enter  numebr - 2 : "))
print(add_numbers(num1, num2))
number_check = int(input("Enter the number to check even or odd : "))
print(is_even(number_check))
# TASK - 2
x = 10 #global
def inside():
    x = 5 #local
    print(f"Inside function : {x}")
inside()
print(f"Outside function : {x}")
