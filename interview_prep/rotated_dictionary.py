import unittest


def find_rotation_point(words):
    lower = 0
    upper = len(words) - 1
    idx = int((upper - lower) / 2)

    if words[-1] < words[-2]:
        return len(words) - 1
    if words[0] < words[-1]:
        return 0

    while upper > lower:
        if words[idx] < words[idx - 1]:
            return idx

        if words[0] > words[idx]:
            upper = idx
        else:
            lower = idx

        idx = int((upper - lower) // 2) + lower


class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    def test_unrotated_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist'])
        expected = 0
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
