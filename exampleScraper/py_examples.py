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
    for i in rw_json.reading_json():
        if i and isinstance(i[0], str) and count_common_words(i[0], message) > 2:
            matching_lists.append(i)
    return matching_lists
