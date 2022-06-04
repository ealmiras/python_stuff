name = input("What is your name? ")
surname = input("What is your surname? ")

if len(name) + len(surname) < 12:
    print(f"{name} {surname} is shorter than the average American name")
elif len(name) + len(surname) > 12:
    print(f"{name} {surname} is longer than the average American name")
else:
    print(f"{name} {surname} is exactly the average length for American names")