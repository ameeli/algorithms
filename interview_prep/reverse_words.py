import unittest


def reverse_words(message):
    """
    Takes a message as a list of characters and reverses the words in place.
    """
    reverse_message(message, 0, len(message) - 1)

    word_start = word_end = 0
    while word_end <= len(message):
        if (word_end == len(message)) or (message[word_end] == ' '):
            reverse_message(message, word_start, word_end - 1)
            word_start = word_end + 1
            word_end = word_start + 1
        else:
            word_end += 1


def reverse_message(message, start, end):
    while start < end:
        message[start], message[end] = message[end], message[start]
        start += 1
        end -= 1


class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
