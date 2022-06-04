# with While Loop - corrected for pluralisation
num = 99
while num > 0:
    if num > 1:
        print(f"\n{num} bottles of beer on the wall.")
        print(f"{num} bottles of beer.")
    else:
        print(f"\n1 bottle of beer on the wall.")
        print(f"1 bottle of beer.")

    if num > 2:
        print(f"Take one down, pass it around, {num-1} bottles of beer on the wall.")
    elif num == 2:
        print(f"Take one down, pass it around, 1 bottle of beer on the wall.")
    else:
        print("Take one down, pass it around, no more bottles of beer on the wall.")  
    num -= 1
  

# with For Loop
for num in range(99, 0, -1):
    print(f"\n{num} bottles of beer on the wall.")
    print(f"{num} bottles of beer.")
    if num != 1:
        print(f"Take one down, pass it around, {num-1} bottles of beer on the wall.")
    else:
        print("Take one down, pass it around, no more bottles of beer on the wall.")   