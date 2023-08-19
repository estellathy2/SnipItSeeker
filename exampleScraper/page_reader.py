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

    print(page.text)
    soup = BeautifulSoup(page.text, 'html.parser')

    output_dict = {}
    
    for code_block_div in soup.find_all("div", {"class": "w3-example"}):
        code = remove_tags(code_block_div.find("div", class_="w3-code notranslate pythonHigh").text) # code block
        title = remove_tags(code_block_div.find("p").text)[:-1] # Title with removed colon
        output_dict[title] = code
    return output_dict
