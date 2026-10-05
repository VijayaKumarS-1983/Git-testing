def hello():
    print("Hello, World!")
def Arithmatic(operation):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Invalid operation"
    return a + b
