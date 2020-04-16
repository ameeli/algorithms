"""
Given an array A of strings made only from lowercase letters, return a list of
all characters that show up in all strings within the list (including
duplicates).  For example, if a character occurs 3 times in all strings but not
4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

Input: ["daaccccd","adacbdda","abddbaba","bacbcbcb","bdaaaddc","cdadacba",
        "bacbdcda","bacdaacd"]
Output: ["a"]

Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""


def find_common_chars(words):
    common_chars = list(words[0])

    for w_i in range(1, len(words)):
        for char_i, char in enumerate(common_chars):
            if char not in words[w_i]:
                common_chars[char_i] = None
            else:
                words[w_i] = words[w_i].replace(char, '', 1)
        common_chars = list(filter(None, common_chars))

    return filter(None, common_chars)


print(find_common_chars(["bella", "label", "roller"]))
print(find_common_chars(["cool", "lock", "cook"]))
print(find_common_chars(["daaccccd", "adacbdda", "abddbaba", "bacbcbcb",
                         "bdaaaddc", "cdadacba", "bacbdcda", "bacdaacd"]))
