# Aug 19, 2023
# W3 Schools Webpage Example Extractor

import requests
from bs4 import BeautifulSoup

def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")
 
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

def find_examples(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    output_list = []
    
    for code_block_div in soup.find_all("div", {"class": "w3-example"}):
        code_div = code_block_div.find("div", class_="w3-code notranslate pythonHigh")
        title_div = code_block_div.find("p")
        if not (title_div is None):
            title = remove_tags(title_div.text)[:-1] # Title
        else:
            title = "Example"
        if not (code_div is None):
            code = remove_tags(code_div.text)
            output_list.append([title,code])

    return output_list

# print(find_examples("https://www.w3schools.com/python/python_strings.asp"))
