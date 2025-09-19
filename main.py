import sys
from stats import get_num_words, get_num_chars, convert_dict_to_list


def get_book_text(path: str) -> str:
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    num_words = get_num_words(get_book_text(path))
    letter_counts = convert_dict_to_list(get_num_chars(get_book_text(path)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k in letter_counts:
        print(f"{k['name']}: {k['num']}")
    print("============= END ===============")


main()
