from random import choice
import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes():
    data = []
    url = "/page/1/"
    while url:
        response = requests.get(BASE_URL + url)
        print(f"Scraping {BASE_URL + url}...")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_ = "quote")

        for quote in quotes:
            data.append({
                "text" : quote.find(class_ = "text").get_text(),
                "author" : quote.find(class_ = "author").get_text(),
                "author_url" : quote.find("a")["href"]
            })
        
        next_btn = soup.find(class_ = "next")
        url = next_btn.find("a")["href"] if next_btn else None  
        sleep(2)
    return data

def write_to_csv():
    with open("quotes.csv", "w") as file:
        headers = ["text","author","author_url"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_to_csv(quotes)