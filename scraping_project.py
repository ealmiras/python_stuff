'''
Web Scraping Project
Introduction
In this project you'll be building a quotes guessing game. When run, your program will scrape a website for a collection of quotes. Pick one at random and display it. The player will have four chances to guess who said the quote. After every wrong guess they'll get a hint about the author's identity.

Requirements
1. Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com
2. You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.
3. Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
    - After each incorrect guess, the number of guesses remaining will decrement. 
        If the player gets to zero guesses without identifying the author, the player loses and the game ends. 
        If the player correctly identifies the author, the player wins!
    - After every incorrect guess, the player receives a hint about the author. 
4. For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.
5. The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.
6. When the game is over, ask the player if they want to play again. 
    If yes, restart the game with a new quote. If no, the program is complete.
Good luck!
'''

from random import choice, random
import requests
from bs4 import BeautifulSoup

first_link = "http://quotes.toscrape.com"

link = first_link
response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all(class_ = "quote")

data = []

page = 1
while True:   
    if soup.find(class_ = "next") is None:
        break

    else:
        for quote in quotes:
            text = quote.find(class_ = "text").get_text()
            author = quote.find(class_ = "author").get_text()
            author_url = quote.find("a")["href"]
            data.append([text, author, author_url])
        
        page += 1
        link = first_link + f"/page/{page}/"

        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_ = "quote")
    
for quote in quotes:
    text = quote.find(class_ = "text").get_text()
    author = quote.find(class_ = "author").get_text()
    author_url = quote.find("a")["href"]
    data.append([text, author, author_url])

repeat = "y"
while repeat == "y":
    q_no = choice(range(len(data)))
    q = data[q_no]
    print("-" * 20)
    print(q[0])
    print("Can you guess who this quote belongs to?")

    try_left = 4
    while try_left > 0:
        try_left -= 1
        print("-" * 20)
        print(f"You have {try_left} tries left!")
        answer = input("Your guess: ")
        
        if answer == q[1]:
            print("-" * 20)
            print(f"Congratulations! Your guess is correct: {answer}.")
            print("-" * 20)
        
        elif try_left == 0:
            print("-" * 20)
            print("That's not correct. The author is: ", (q[1]).upper())
            print("-" * 20)
        
        else:
            print("-" * 20)           
            print("That's not correct, try again! Here is a hint for you.")
            
            author_link = first_link+q[2]
            response = requests.get(author_link)
            soup = BeautifulSoup(response.text, "html.parser")
            
            if try_left == 3:
                date = soup.find(class_ = "author-born-date").get_text()
                location = soup.find(class_ = "author-born-location").get_text()
                hint = f"The author was born in {date} {location}"
                print(hint)
            
            elif try_left == 2:
                first_first = q[1][0]
                hint = f"The first letter of the author's first name is: '{first_first}'"
                print(hint)
            
            else:
                name = q[1].split(" ")
                last_first = name[len(name)-1][0]
                hint = f"The first letter of the author's last name is: {last_first}"
                print(hint)
 
    repeat = input("Would you like to play again? (y/n): ")