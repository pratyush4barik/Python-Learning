total_students = int(input("Enter the total number of students: "))
student_info = []
for i in range(total_students):
    # Collecting student information
    print(f"Student {i + 1} : ")
    student = {
        "name" : input(f"Enter the name of student {i + 1} : "),
        "Roll No" : input(f"Enter the roll number of student {i + 1} : "),
        "age" : int(input(f"Enter the age of student {i + 1} : ")),
        "marks" : int(input(f"Enter the marks of student {i + 1} : "))
    }
    student_info.append(student) # Adding student information to the list
print(student_info, end = "\n")  # Printing the list of student information

