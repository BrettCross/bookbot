def get_book_text(filepath):
    """takes a filepath as input and returns the contents of the file as a string."""
    
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(string):
    """takes a string as input and returns the number of words in the string."""
    words = string.split()
    count = 0

    for word in words:
        count += 1
    
    return count

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)

    print(f"{num_words} words found in the document")


main()
