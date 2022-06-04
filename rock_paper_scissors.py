from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    c_move = "rock"
elif num == 2:
    c_move = "paper"
else:
    c_move = "scissors"

# Ask a user to enter their move
u_move = input("\nPlease enter your move (rock/paper/scissors): ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print(f"\nYour move is {u_move.upper()}:")
if u_move == "rock":
    print(rock)
elif u_move == "paper":
    print(paper)
else:
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(f"\nComputer's move is {c_move.upper()}:")
if c_move == "rock":
    print(rock)
elif c_move == "paper":
    print(paper)
else:
    print(scissors)

# Figure out who wins and print the result!
tie = u_move == c_move
win = u_move == "rock" and c_move == "scissors" or u_move == "scissors" and c_move == "paper" or u_move == "paper" and c_move == "rock"

if tie:
    print("\nIt's a tie!\n")
elif win:
    print("\nYou win!\n")
else:
    print("\nYou lose!\n")