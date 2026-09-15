import unittest

from word_count import count_words


class TestCountWords(unittest.TestCase):
    def test_basic_sentence(self):
        result = count_words("the cat sat on the mat")
        self.assertEqual(
            result, {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
        )

    def test_empty_string(self):
        self.assertEqual(count_words(""), {})

    def test_case_and_punctuation_are_normalized(self):
        result = count_words("Hello, hello! HELLO world.")
        self.assertEqual(result, {"hello": 3, "world": 1})


if __name__ == "__main__":
    unittest.main()
