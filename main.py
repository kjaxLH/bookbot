from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_file = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    text = get_book_text(book_file)
    word_count = get_word_count(text)
    #print(f"{word_count} words found in the document") 
    char_counts = get_char_count(text)
    #print(char_counts)
    sorted = sort_dict(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

main()