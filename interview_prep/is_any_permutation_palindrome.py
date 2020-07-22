import unittest


def has_palindrome_permutation(the_string):
    """
    Given a string, check if any permutations of that string will be a
    palindrome.
    """
    letter_counts = {}
    odd_count = False

    for letter in the_string:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for letter, count in letter_counts.items():
        if count % 2 != 0:
            if odd_count:
                return False
            odd_count = True

    return True


def has_palindrome_permutation(the_string):
    """Solution with better space complexity."""
    unpaired_chars = set()

    for char in the_string:
        if char in unpaired_chars:
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    return len(unpaired_chars) <= 1


class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
