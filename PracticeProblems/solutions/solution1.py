# Create a simple calculator in python

#Take Input from user
digit1 = input("First number: ")
operation = input("Operation (+, -, *, /): ")
digit2 = input("Second number: ")

if operation == "+":
    print(f"Answer: {int(digit1) + int(digit2)}")
elif operation == "-":
    print(f"Answer: {int(digit1) - int(digit2)}")
elif operation == "*":
    print(f"Answer: {int(digit1) * int(digit2)}")
elif operation == "/":
    print(f"Answer: {int(digit1) / int(digit2)}")
else:
    print("Invalid input!")
