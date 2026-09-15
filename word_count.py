import string


def count_words(text):
    """Return a dict mapping each word in text to its frequency.

    Matching is case-insensitive and ignores surrounding punctuation.
    """
    counts = {}
    for raw_word in text.split():
        word = raw_word.strip(string.punctuation).lower()
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts
