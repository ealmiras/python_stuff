unit = input("\nWhat unit are you using?(f/c/k) ")
temp = int(input("What temperature is the water? "))

f_boiling = 212
c_boiling = 100
k_boiling = 373

if unit == "f":
    if temp > f_boiling:
        print("The water is boiling")
    else:
        print(f"Water boils at {f_boiling} degrees fahrenheit\n")
elif unit == "c":
    if temp > c_boiling:
        print("The water is boiling")
    else:
        print(f"Water boils at {c_boiling} degrees celcius\n")
else:
    if temp > k_boiling:
        print("The water is boiling")
    else:
        print(f"Water boils at {k_boiling} degrees kelvin\n")