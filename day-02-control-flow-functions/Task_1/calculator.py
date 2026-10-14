
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    choice = input(
        "\nChoose operation (+, -, *, /) or type 'end' to exit: "
    ).lower()

    if choice == "end":
        print("Calculator closed!")
        break

    if choice not in ["+", "-", "*", "/"]:
        print("Invalid operation!")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    match choice:
        case "+":
            print("Result:", add(a, b))
        case "-":
            print("Result:", subtract(a, b))
        case "*":
            print("Result:", multiply(a, b))
        case "/":
            print("Result:", divide(a, b))
