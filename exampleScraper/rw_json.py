import json
import page_reader

def reading_json():
    with open('numbers.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    return(json_object)

def writing_json():
    filename = 'examples.json'
    with open(filename, 'w') as file_object:  #open the file in write mode
        json.dump(page_reader.find_examples(), file_object)