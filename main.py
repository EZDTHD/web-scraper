import requests
import csv
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find_all("h2", class_="mod-Treffer__name")
nummer = soup.find_all("a", class_="mod-TelefonnummerKompakt__phoneNumber")
with open("info.csv", "w")as f:
    for i in title:
        f.write(i.text.strip() + "\n")
    for i in nummer:
        f.write(i.text.strip()+ "\n")
