from random import choice
import requests
from bs4 import BeautifulSoup
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = choice(quotes)
    try_left = 4

    print("-" * 20)
    print(quote["text"])
    print("Can you guess who this quote belongs to?")

    while try_left > 0:
        try_left -= 1
        print("-" * 20)
        print(f"You have {try_left} tries left!")
        answer = input("Your guess: ")
        
        if answer.lower() == quote["author"].lower():
            print("-" * 20)
            print(f"Congratulations! Your guess is correct: {answer}.")
            print("-" * 20)
            break
        
        elif try_left == 0:
            print("-" * 20)
            print("That's not correct. The author is: ", (quote["author"]).upper())
            print("-" * 20)
        
        else:
            print("-" * 20)           
            print("That's not correct, try again! Here is a hint for you.")
            
            author_link = BASE_URL + quote["author_url"]
            response = requests.get(author_link)
            soup = BeautifulSoup(response.text, "html.parser")
            
            if try_left == 3:
                date = soup.find(class_ = "author-born-date").get_text()
                location = soup.find(class_ = "author-born-location").get_text()
                hint = f"The author was born in {date} {location}"
                print(hint)
            
            elif try_left == 2:
                first_first = quote["author"][0]
                hint = f"The first letter of the author's first name is: '{first_first}'"
                print(hint)
            
            else:
                name = quote["author"].split(" ")
                last_first = name[len(name)-1][0]
                hint = f"The first letter of the author's last name is: {last_first}"
                print(hint)
    
    repeat = ""
    while repeat.lower() not in ("yes", "y", "no", "n"):
        repeat = input("Would you like to play again? (y/n): ")
    if repeat.lower() in ("y", "yes"):
        return start_game(quotes)
    else:
        print("OK, Goodbye!")

quotes = read_quotes("quotes.csv")
start_game(quotes)