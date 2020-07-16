import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    prev_permutations = get_permutations(all_chars_except_last)
    curr_permutations = set()

    for permutation in prev_permutations:
        for position in range(len(all_chars_except_last) + 1):
            new_permutation = (permutation[:position]
                               + last_char
                               + permutation[position:])
            curr_permutations.add(new_permutation)

    return curr_permutations


class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
