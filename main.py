# Import the 'get_num_words' function from the 'stats.py' file
from stats import get_num_words, get_num_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"Found {num_words} total words")
    print(num_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

