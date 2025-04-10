def get_num_words(string):
    """takes a string as input and returns the number of words in the string."""
    words = string.split()
    count = 0

    for word in words:
        count += 1
    
    return count

def count_characters(string):
    """text from the book as a string, and returns the number of times each 
    character, (including symbols and spaces), appears in the string."""
    chars = {}
    words = string.split()

    for word in words:    
        for i in range(0, len(word)):
            char = word[i].lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    
    return chars

def sort_on(d):
    return d["count"]

def sort_chars(d):
    """takes the dictionary of chars and their counts and returns a sorted list of dictionaries."""
    arr = []
    for key in d:
        arr.append({"char":key, "count":d[key]})

    arr.sort(reverse=True, key=sort_on)
    return arr
