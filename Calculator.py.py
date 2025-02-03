def calculator():
    print("Options: +, -, *, /")
    operation = input("Choose operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operation!")
