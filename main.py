# First Function reads in book.
def get_book_text(book_file):
    with open(book_file) as bf:
        print(bf)

def main():
    path = "books/frankenstein.txt"
    book_string = get_book_text(path)
    print(book_string)

main()
