def get_book_text(path: str) -> str:
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()

    return file_contents


def count_words(text: str) -> int:
    return len(text.split())


def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")


main()
