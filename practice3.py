# DAY - 4
input = int(input("Enter the number : "))
i = 1
while i<=10:
    print(f"{input} x {i} = {input *i}")
    i += 1
# This code takes an integer input from the user and prints its multiplication table from 1 to 10.
# Now printing all even  number from 1 to 50 using for loop
print("Even numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
    i += 1