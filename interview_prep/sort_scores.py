import unittest
"""
Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(nlgn) time.

For example:

  unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)

Python 3.6
We’re defining n as the number of unsorted_scores because we’re expecting the
number of players to keep climbing.

And, we'll treat highest_possible_score as a constant instead of factoring it
into our big O time and space costs because the highest possible score isn’t
going to change. Even if we do redesign the game a little, the scores will stay
around the same order of magnitude.

Gotchas
Multiple players can have the same score! If 10 people got a score of 90, the
number 90 should appear 10 times in our output list.

We can do this in O(n) time and space.
"""


def sort_scores(unsorted_scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score + 1)
    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []
    for score in range(highest_possible_score, 0, -1):
        curr_count = score_counts[score]
        while curr_count > 0:
            sorted_scores.append(score)
            curr_count -= 1

    return sorted_scores


class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
