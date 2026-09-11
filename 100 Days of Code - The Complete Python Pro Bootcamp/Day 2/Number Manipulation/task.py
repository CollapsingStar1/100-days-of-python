# 1. Take user input (both inputs are received as strings)
height = input("Enter your height in meters (e.g. 1.75): ")
weight = input("Enter your weight in kg (e.g. 70): ")

# 2. Convert string inputs to floating point numbers
weight_as_float = float(weight)
height_as_float = float(height)

# 3. Calculate BMI using the exponent operator (**)
bmi = weight_as_float / (height_as_float ** 2)

# 4. Round the result to 2 decimal places (or convert with int() for a whole number)
bmi_rounded = round(bmi, 10)
bmi_as_int = int(bmi)

# 5. Output using an f-string
print(f"Your exact BMI is {bmi_rounded}")
print(f"Your floored whole number BMI is {bmi_as_int}")