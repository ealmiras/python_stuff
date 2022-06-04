print("\nWELCOME TO THE GAME!\n")

player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")
print("\nYou can take 1, 2, or 3 toothpicks at a time. Whoever takes the last one, wins the game!\n")

num = 13

while True:
    print("| " * num)
    print(f"There are {num} toothpicks left.")
    p1 = int(input(f"How many toothpicks do you take {player1}: "))
    num -= p1
    if num <= 0:
        print(f"{player1.upper()} wins!")
        break
    print("|" * num)
    print(f"There are {num} toothpicks left.")
    p2 = int(input(f"How many toothpicks do you take {player2}: "))
    num -= p2
    if num <= 0:
        print(f"\n{player2.upper()} wins!")
        break 
print("GAME OVER!")
