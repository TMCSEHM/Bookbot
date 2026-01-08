# Import the 'get_num_words' function from the 'stats.py' file
from stats import get_num_words, get_num_chars, convert_dict_to_list, sort_on, sort_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    num_chars_list = convert_dict_to_list(num_chars)
    sorted_char_num = sort_dict(num_chars_list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_char_num:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

