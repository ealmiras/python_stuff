import sqlite3
import requests
from bs4 import BeautifulSoup

url = ("http://books.toscrape.com/catalogue/category/books/history_32/index.html")

# Main method!
def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    save_books(all_books)

# Scrape the data
def get_title(book):
    return book.find("h3").find("a")["title"]
def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("Â","").replace("£",""))
def get_rating(book):
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    rating = book.select(".star-rating")[0].get_attribute_list("class")[1]
    return ratings[rating]    

# Save the data to database 
def save_books (all_books):
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE books
        (title TEXT, price REAL, rating INTEGER)""")
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    conn.commit()
    conn.close()


scrape_books(url)