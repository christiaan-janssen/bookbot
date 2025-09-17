def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_chars(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text:
        for c in word:
            c = c.lower()
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

    return counts
