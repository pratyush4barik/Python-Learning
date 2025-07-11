# DAY - 3
age = int(input("Enter your age : "))
exam_score = int(input("Enter your exam score : "))
# Use of conditional statements with if, elif, else and logical operators
# for age
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
# for exam score
if exam_score < 60:
    print("GRADE : D")
elif exam_score < 75:
    print("GRADE : C")
elif exam_score < 90:
    print("GRADE : B")
else:
    print("GRADE : A")