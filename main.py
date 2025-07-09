# Import stats file for function calls
from stats import get_word_count

# First Function reads in book.
def get_book_text(book_file):
    with open(book_file) as bf:
        str = bf.read()
        return str

def main():
    path = "books/frankenstein.txt"
    book_string = get_book_text(path)
    wc = get_word_count(book_string)
    print(f"{wc} words found in the document")

main()
