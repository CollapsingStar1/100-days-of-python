import inspect
import math

import art
print(art.logo)
# --- Operation Definitions ---
def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2): return "Error: Division by zero" if n2 == 0 else n1 / n2
def power(n1, n2): return n1 ** n2
def square(n1): return n1 ** 2
def square_root(n1): return math.sqrt(n1)
def cube(n1): return n1 ** 3
def factorial(n1): return math.factorial(int(n1))
def percent(n1, n2): return n1 * (n2 / 100)
def median_3(n1, n2, n3): return sorted([n1, n2, n3])[1]

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "sq": square,
    "sqrt": square_root,
    "cube": cube,
    "!": factorial,
    "%": percent,
    "med3": median_3,
}



def calculator():
    print("Available operators:", " ".join(operations.keys()))

    current_result = None

    while True:
        # If starting fresh, ask for first number
        if current_result is None:
            current_result = float(input("\nEnter first number: "))

        op_symbol = input(f"Pick an operation ({' '.join(operations.keys())}): ").strip()

        if op_symbol not in operations:
            print("Invalid operator!")
            continue

        func = operations[op_symbol]
        param_count = len(inspect.signature(func).parameters)

        # Build arguments dynamically
        args = [current_result]
        for i in range(2, param_count + 1):
            args.append(float(input(f"Enter argument {i}: ")))

        # Execute function by unpacking args
        result = func(*args)

        if isinstance(result, str):  # Caught division by zero or error
            print(result)
            current_result = None
            continue

        print(f"Result: {result}")
        current_result = result

        choice = input(f"Type 'y' to continue with {current_result}, 'n' to start fresh, or 'exit': ").lower().strip()
        if choice == 'n':
            current_result = None
        elif choice == 'exit':
            print("Goodbye!")
            break


calculator()