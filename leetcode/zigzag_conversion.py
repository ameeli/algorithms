import unittest

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number
of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


def convert_to_zigzag(s, num_rows):
    if num_rows == 1:
        return s

    rows = [''] * num_rows
    row = 0
    increasing = True

    for char in s:
        rows[row] += char

        if row == num_rows - 1:
            increasing = False
        if row == 0:
            increasing = True

        if increasing:
            row += 1
        else:
            row -= 1

    return ''.join(rows)


class TestConvertToZigzag(unittest.TestCase):
    def test_four_rows(self):
        actual = convert_to_zigzag('PAYPALISHIRING', 4)
        expected = 'PINALSIGYAHRPI'
        self.assertEqual(actual, expected)

    def test_three_rows(self):
        actual = convert_to_zigzag('PAYPALISHIRING', 3)
        expected = 'PAHNAPLSIIGYIR'
        self.assertEqual(actual, expected)

    def test_one_row(self):
        actual = convert_to_zigzag('PAYPALISHIRING', 1)
        expected = 'PAYPALISHIRING'
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
