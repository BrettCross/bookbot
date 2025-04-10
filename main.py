from stats import get_num_words

def get_book_text(filepath):
    """takes a filepath as input and returns the contents of the file as a string."""
    
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)

    print(f"{num_words} words found in the document")


main()
