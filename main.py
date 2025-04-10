import sys
from stats import get_num_words
from stats import count_characters
from stats import sort_chars

def get_book_text(filepath):
    """takes a filepath as input and returns the contents of the file as a string."""
    
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def pretty_print(filepath, total_words, char_dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_dict_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

        text = get_book_text(filepath)

        num_words = get_num_words(text)

        char_dict = count_characters(text)

        char_dict_list = sort_chars(char_dict)

        pretty_print(filepath, num_words, char_dict_list)


main()
