print("\nWELCOME TO THE GAME!\n")

player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")
print("\nYou can take 1, 2, or 3 toothpicks at a time. Whoever takes the last one, wins the game!\n")

num = 13
current_player = player1

while True:
    print("| " * num)
    print(f"There are {num} toothpicks left.")
    pick = int(input(f"How many toothpicks do you take {current_player}: "))
    while pick != 3 and pick != 2 and pick != 1:
        pick = int(input("You can only take 1, 2, or 3: "))
    num -= pick
    if num <= 0:
        print(f"\n{current_player.upper()} wins!")
        break
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
print("\nGAME OVER!")
