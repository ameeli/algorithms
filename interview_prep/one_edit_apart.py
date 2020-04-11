"""
Write a function that returns whether two words are exactly "one edit" away
using the following signature:
bool OneEditApart(string s1, string s2);

An edit is:
Inserting one character anywhere in the word (including at the beginning and end)
Removing one character
Replacing one character

Examples:
OneEditApart("cat", "dog") = false
OneEditApart("cat", "cats") = true
OneEditApart("cat", "cut") = true
OneEditApart("cat", "cast") = true
OneEditApart("cat", "at") = true
OneEditApart("cat", "act") = false
"""


def is_one_edit_away(str1, str2):
    str1_idx = 0
    str2_idx = 0
    edits = 0

    while str1_idx < len(str1) and str2_idx < len(str2):
        if abs(len(str1) - len(str2)) > 1:
            return False
        if str1[str1_idx] == str2[str2_idx]:
            str1_idx += 1
            str2_idx += 1
        else:
            if len(str1) == len(str2):
                str1_idx += 1
                str2_idx += 1
            elif len(str1) > len(str2):
                str1_idx += 1
            else:
                str2_idx += 1

            edits += 1
            if edits > 1:
                return False

    return True


print(is_one_edit_away("cat", "dog"), False)
print(is_one_edit_away("cat", "cats"), True)
print(is_one_edit_away("cat", "cut"), True)
print(is_one_edit_away("cat", "cast"), True)
print(is_one_edit_away("cat", "at"), True)
print(is_one_edit_away("cat", "act"), False)
