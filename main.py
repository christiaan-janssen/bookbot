from stats import get_num_words, get_num_chars


def get_book_text(path: str) -> str:
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()

    return file_contents


def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    char_counts = get_num_chars(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(char_counts)


main()
