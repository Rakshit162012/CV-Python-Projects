python
def calculator():
    print("Welcome to the Python Calculator!")
    try:
        a = float(input("First number: "))
        op = input("Operator (+, -, *, /): ").strip()
        b = float(input("Second number: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                return "Error: division by zero is not allowed."
            result = a / b
        else:
            return "Error: unknown operator."

        return f"Result: {result}"
    except ValueError:
        return "Error: please enter valid numbers."

if __name__ == "__main__":
    print(calculator())
