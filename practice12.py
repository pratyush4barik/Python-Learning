# DAY - 13
# File handling in python
name = input("Enter your name : ")
roll_no = int(input("Enter the Roll no :"))
marks = int(input("Enter the marks :"))
file = open("student_data.txt", "w") # writing inside the file
file.write(f"Name : {name}\n")
file.write(f"Roll no : {roll_no}\n")
file.write(f"Marks : {marks}\n")
file.close()
with open("student_data.txt", "r") as file: # reading the file
    data = file.read()
    print("FIle Contains : ")
    print(data)
