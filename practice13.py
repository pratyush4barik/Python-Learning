# Day 14
#Exception Handling
try:
    x = int(input("Enter Number - 1 : "))
    y = int(input("Enter Number - 2 : "))
    op = input("Enter Operation (+, -, *, /) : ")

    if op == '+' :
        print(f"Addition : {x + y}")
    elif op == '-' :
        print(f"Substraction : {x - y}")
    elif op == '*' :
        print(f"Multiplication : {x * y}")
    elif op == '/' :
        print(f"Division : {x / y}")
    else:
        print("Invalid Operator.")
    
except ZeroDivisionError:
    print("Cannot Divide by Zero.")
except ValueError:
    print("Please enter valid numbers.")
finally:
    print("Program Finished.")