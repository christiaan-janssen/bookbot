def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_chars(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text:
        for c in word:
            c = c.lower()
            if c.isalpha():
                if c in counts:
                    counts[c] += 1
                else:
                    counts[c] = 1

    return counts


def sort_on(items):
    return items["num"]


def convert_dict_to_list(char_counts: dict[str, int]) -> list[dict[str, int]]:
    l = []
    for k, v in char_counts.items():
        l.append({"name": k, "num": v})
    l.sort(reverse=True, key=sort_on)
    return l
