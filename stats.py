def get_num_words(string):
    """takes a string as input and returns the number of words in the string."""
    words = string.split()
    count = 0

    for word in words:
        count += 1
    
    return count