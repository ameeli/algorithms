def reverse(list_of_chars):
    """Reverse list in place"""
    for i in range(len(list_of_chars)/2):
        list_of_chars[i], list_of_chars[-i - 1] = list_of_chars[-i - 1], list_of_chars[i]