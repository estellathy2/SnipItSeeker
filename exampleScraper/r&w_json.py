import json
import page_reader

def reading_json():
    with open('examples.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    print(json_object)
    print(type(json_object))

def writing_json(url):
    filename = 'examples.json'
    with open(filename, 'w') as file_object:  #open the file in write mode
        json.dump(page_reader.find_examples(url), file_object)

reading_json()
