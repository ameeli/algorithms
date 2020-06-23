"""Parse an unbroken sentence into possible words.

Example:

    >>> sentences = parse('iatenoodlesfordinnertonight', vocab)

    >>> for s in sorted(sentences):
    ...    print(s)
    i a ten oodles for dinner to night
    i a ten oodles for dinner tonight
    i a ten oodles ford inner to night
    i a ten oodles ford inner tonight
    i ate noodles for dinner to night
    i ate noodles for dinner tonight
    i ate noodles ford inner to night
    i ate noodles ford inner tonight

"""

vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night',
         'ate', 'noodles', 'for', 'dinner', 'tonight'}


# def parse(phrase, vocab):
#     """Break a string into words.

#     Input:
#         - string of words without space breaks
#         - vocabulary (set of allowed words)

#     Output:
#         set of all possible ways to break this down, given a vocab
#     """

def parse(phrase, vocab):
    """Break a string into words.

    Input:
        - string of words without space breaks
        - vocabulary (set of allowed words)

    Output:
        set of all possible ways to break this down, given a vocab
    """

    # START SOLUTION

    possible_breaks = set()

    # idea: find all words that match beginning of string
    # and recursively parse the remainder of string

    for word in vocab:
        print('word:', word)
        print('phrase', phrase)
        if phrase == word:
            # base case: no parsing required; add word to result set
            possible_breaks.add(word)

        elif phrase.startswith(word):
            # general case: word matches beginning of string

            rest = phrase[len(word):]  # rest of string

            # Use this word and recurse to solve the rest of it
            word_and_rest = {word + ' ' + parsed
                             for parsed in parse(rest, vocab)}
            print('word_and_rest', word_and_rest)

            # finished answer to list of answers
            possible_breaks.update(word_and_rest)
            print('possible_breaks', possible_breaks)

    return possible_breaks


print(parse('iatenoodlesfordinnertonight', vocab))
# if __name__ == '__main__':
#     import doctest

#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TESTS PASSED; GREAT JOB! ***\n")
