import random

num_dice = input("How many dice are we rolling? ")
while not num_dice.isnumeric():
    num_dice = input("How many dice are we rolling? ")
num_dice = int(num_dice)

num_side = input("How many sides on each dice? ")
while not num_side.isnumeric():
    num_side = input("How many sides on each dice? ")
num_side = int(num_side)


while True:
    x = "|"
    for i in range(num_dice):
        x = x + str(random.randint(1,num_side)) + "|"
    print(x)
    replay = input("Roll again? ('q' to quit)")
    if replay == "q":
        break
