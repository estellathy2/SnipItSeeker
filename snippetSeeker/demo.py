import gradio as gr

import rw_json

def search_keyword(keyword):
    matching_lists = []
    for i in rw_json.reading_json():
        if i and isinstance(i[0], str) and keyword in i[0]:
            matching_lists.append(i)
    return matching_lists

def count_common_words(str1, str2):
    words1 = str1.lower().split()
    words2 = str2.lower().split()
    return len(set(words1) & set(words2))

def search_similarity(message):
    message = str(message)
    matching_lists = []
    count = 0
    words_in_message = message.lower().split()
    
    if len(words_in_message) < 4:  # If message has less than 4 words
        for i in rw_json.reading_json():
            if count >= 10:
                break
            if i and isinstance(i[0], str) and all(word in i[0].lower() for word in words_in_message):
                matching_lists.append(i)
                count += 1
    else:  # If message has 4 or more words
        for i in rw_json.reading_json():
            if count >= 10:
                break
            if i and isinstance(i[0], str) and count_common_words(i[0], message) >= 4:
                matching_lists.append(i)
                count += 1
    
    return matching_lists
    
def code_response(message, history):
    message = str(message)
    matching_lists = search_similarity(message)
    output = '\n\n'.join([f"{item[0]}\n```py\n{item[1]}\n```" for item in matching_lists])
    return output

gr.ChatInterface(code_response).launch(share=True)
