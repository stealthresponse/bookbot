# Import stats file for function calls and sys for cmd calls
import sys
from stats import get_char_count, get_sorted_dict, get_word_count

# First Function reads in book.
def get_book_text(book_file):
    with open(book_file) as bf:
        str = bf.read()
        return str

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        book_string = get_book_text(path)
        wc = get_word_count(book_string)
        char_count = get_char_count(book_string)
        sorted_dict = get_sorted_dict(char_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {wc} total words")
        print("----------- Character Count ----------")
        for pair in sorted_dict:
            for k, v in pair.items():
                print(f"{k}: {v}")

main()
