import requests
from bs4 import BeautifulSoup
from csv import writer

link = "https://rithmschool.com/blog"

response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
    
while soup.find(class_ = "next"):
    i = 2
    link = link + "?page=" + str(i)

    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")

    with open("blog_data.csv", "w") as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(["title", "link", "date"])

        for article in articles:
            a_tag = article.find("a")
            title = a_tag.get_text()
            url = a_tag["href"]
            date = article.find("time")["datetime"]
            csv_writer.writerow([title, url, date])
    
    i += 1