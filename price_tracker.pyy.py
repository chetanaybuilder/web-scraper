import requests
from bs4 import BeautifulSoup
import json

url = "https://books.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")

price_data = []

for book in books:
    title = book.find("h3").text
    price = book.find("p", class_="price_color").text

    price_data.append({
        "title": title,
        "price": price
    })

with open("price_history.json", "w") as file:
    json.dump(price_data, file, indent=4)

print("Data saved successfully!")