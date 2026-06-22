import requests
from bs4 import BeautifulSoup
url = "https://example.com/product"
old_price = 60000
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
user_email = "client@gmail.com"
current_price = 55000
if current_price < old_price:
    print(" price dropped!")
    print(f"sending alert to {user_email}")
else:
    print("price not dropped!")