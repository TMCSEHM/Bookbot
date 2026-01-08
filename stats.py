def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    for c in text:
        # Check for *lowercase* version!
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#def convert_dict_to_list(chars_dict):
 #   result_list = []
  #  for char, num in chars_dict.items():
   #     new_dict = {
    #            "char": char, 
     #           "num": num
      #          }
        ## .append here otherwise += makes a mess of it
       # result_list.append(new_dict)
    #return result_list

def sort_on(chars_dict):
    return chars_dict["num"]
    
#def sort_dict(chars):
 #   chars.sort(reverse=True, key=sort_on)
  #  return chars


# "Correct" way to do it, didn't learn .items yet
def convert_dict_to_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

