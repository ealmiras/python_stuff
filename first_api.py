import requests
from random import choice
import pyfiglet
import termcolor

header = termcolor.colored(
    pyfiglet.figlet_format("Dad Jokes 3000"),
    "red")
print(header)

url = "https://icanhazdadjoke.com/search"
topic = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()

num_jokes = response["total_jokes"]
jokes = response["results"]

if num_jokes > 1:
    print(f"There are {num_jokes} jokes about {topic}! Here is one:")
    print(choice(jokes)["joke"])
elif num_jokes == 1:
    print("There is one joke about {topic}! Here it is:")
    print(jokes[0]["joke"])
else:
    print(f"Sorry, I couldn't find any joke about {topic}!")
