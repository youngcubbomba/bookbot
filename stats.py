def count_words(text):
    words = text.split()
    return len(words)
def times_char(text):
    text = text.lower()
    numb_char = {}
    for ch in text:
        if(ch in numb_char):
            numb_char[ch] = numb_char[ch]+1
        else:
            numb_char[ch] = 1
    return numb_char
def sort_on(items):
    return items["num"]
def sort_dictionary(char_counts):
    sorted_counts = []
    for key in char_counts:
        entry = {"char": key, "num":char_counts[key]}
        sorted_counts.append(entry)
    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts
    