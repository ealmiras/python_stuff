print("\nHI THERE! WELCOME TO THE SHOPPING APP!")
print("**************************************\n")

item = input("What would you like to buy? ")
price = input(f"What is the price of the {item}? ")
quantity = input(f"How many {item} are you buying? ")

print(f"\n{quantity} {item}(s) are added to the cart!")
print(f"Subtotal: ${float(price) * int(quantity)}\n")