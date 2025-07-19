def get_word_count(text):
    text_as_list = text.split()
    count = len(text_as_list)
    return count

def get_char_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_dict(dict):
    new_list = []
    for char in dict:
        new_list.append( {"char" : char, "num": dict[char]})

    def sort_on(items):
        return items["num"]

    new_list.sort(reverse=True, key=sort_on)
    return(new_list)