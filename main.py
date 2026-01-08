import sys
# Import the 'get_num_words', ... functions from the 'stats.py' file
from stats import (
        get_num_words, 
        get_num_chars, 
        convert_dict_to_list, 
        #sort_on, 
        #sort_dict,
        )

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars_list = convert_dict_to_list(num_chars)
    #sorted_char_num = sort_dict(num_chars_list)
    print_report(book_path, num_words, sorted_chars_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    #for item in sorted_char_num:
     #   char = item["char"]
      #  num = item["num"]
       # if char.isalpha():
        #    print(f"{char}: {num}")

    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")


main()

