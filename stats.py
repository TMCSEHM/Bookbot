def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    num_chars = {}
    for char in text:
        # Check for *lowercase* version!
        if char.lower() in num_chars:
            num_chars[char.lower()] += 1
        else:
            num_chars[char.lower()] = 1
    return num_chars

