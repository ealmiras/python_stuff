
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
print("\n")
for char in word:
    print(char)
    
# Write a while loop that does the same thing!
char = 0
print("\n")
while char < len(word):
    print(word[char])
    char += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
num = 100
print("\n")
while num <= 140:
    print(num)
    num += 2

# Write a for loop that does the same thing (with range())
print("\n")
for num in range(100, 141, 2):
    print(num)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
print("\n")
answer = input("Write here 'sillygoose': ")
while answer != "sillygoose":
    answer = input("Hey, listen to me! Write here 'sillygoose': ")
print("Thank you, sillygoose!")