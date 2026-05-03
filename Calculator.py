def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        print(f"Result: {result}\n")

        again = input("Calculate again? (yes/no): ")
        if again.lower() != "yes":
            break

if __name__ == "__main__":
    calculator()