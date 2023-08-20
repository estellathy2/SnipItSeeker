# Aug 19, 2023
# W3 Schools Crawler

import page_reader
import requests
from bs4 import BeautifulSoup

def get_all_examples():
    home_page = requests.get("https://www.w3schools.com/python/")
    soup = BeautifulSoup(home_page.text, 'html.parser')
    examples = []
    # Visits all items in the left menu
    for item in soup.find("div",{"id":"leftmenuinnerinner"}).find_all("a", href=True):
        examples += page_reader.find_examples(f"https://www.w3schools.com/python/{item['href']}")
    return examples

def _print_all_examples():
    for i in get_all_examples():
        print(i[0])
        print(i[1])
        print("")
