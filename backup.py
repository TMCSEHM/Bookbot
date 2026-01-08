def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = string_to_words(text)
    print(f"Found {num_words} total words")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def string_to_words(file_contents):
    num_word = 0
    words = file_contents.split()
    for i in range(0, len(words)):
        num_word += 1
    return num_word

main()
