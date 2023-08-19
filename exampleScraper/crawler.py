# Aug 19, 2023
# W3 Schools Crawler

import page_reader
import requests
from bs4 import BeautifulSoup

home_page = requests.get("https://www.w3schools.com/python/")
soup = BeautifulSoup(home_page.text, 'html.parser')

# Visits all items in the left menu
for item in soup.find("div",{"id":"leftmenuinnerinner"}).find_all("a", href=True):
    print(page_reader.find_examples(f"https://www.w3schools.com/python/{item['href']}"))
