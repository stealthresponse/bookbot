# Takes in book_string and returns an integer of the number of words in the book.
def get_word_count(book_string):
    num = len(book_string.split())
    return num

# Takes in book_string and returns a Dictionary. Counts appearance of all chars+symbols
# in lowercase.
def get_char_count(book_string):
    char_dict = {}
    for char in list(book_string):
        if char.lower() not in char_dict:
            char_dict.update({char.lower(): 1})
        else:
            char_dict[char.lower()] += 1
    return char_dict
