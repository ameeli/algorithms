'''
Find the index of an item in a list using recursion.

Given a list of items:

    >>> lst = ["hey", "there", "you"]

You should have a function that returns the 0-based index of a sought item:

    >>> recursive_search("hey", lst)
    0

    >>> recursive_search("you", lst)
    2

If the item isn't in the list, return None:

    >>> recursive_search("folks", lst)
    None
'''

def recursive_index(needle, haystack):
    def helper(needle, haystack, index):
        if index >= len(haystack):
            return None
        if haystack[index] == needle:
            return index
        return helper(needle, haystack, index + 1)
    
    return helper(needle, haystack, 0)