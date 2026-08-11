def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        return "Invalid input"
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return f"BMI: {bmi:.2f} ({category})"

# Demo run
print(calculate_bmi(60, 1.65))
