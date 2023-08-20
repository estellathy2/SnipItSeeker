# rw_json.py
# Copyright (c) 2023 Estella Tang and Andy Yu
# This project is licensed under the MIT License. See LICENSE for details.

import json
import crawler

def reading_json():
    with open('examples.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    return(json_object)

def writing_json():
    filename = 'examples.json'
    with open(filename, 'w') as file_object:  #open the file in write mode
        json.dump(crawler.get_all_examples(), file_object)
