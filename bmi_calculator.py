height = float(input("\nEnter your height in meters: "))
weight = float(input("Enter your weight in kgs: "))

bmi = round(weight / (height**2),2)

# < 16.0    Severely Underweight 
# 16.0 - 18.4   Underweight
# 18.5 - 24.9   Normal
# 25.0 - 29.9   Overweight
# 30.0 - 34.9   Moderately Obese
# 35.0 - 39.9   Severely Obese
# > 39.9   Morbidly Obese

if bmi < 16.0:
    category = "Severely Underweight"
elif bmi < 18.4:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal"
elif bmi < 29.9:
    category = "Overweight"
elif bmi < 34.9:
    category = "Moderately Obese"
elif bmi < 39.9:
    category = "Severely Obese"
else:
    category = "Morbidly Obese"

print(f"\nYour BMI is {bmi}, which makes you {category}\n")