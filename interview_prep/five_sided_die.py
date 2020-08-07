import random

"""
You have a function rand7() that generates a random integer from 1 to 7. Use it
to write a function rand5() that generates a random integer from 1 to 5.

rand7() returns each integer with equal probability. rand5() must also return
each integer with equal probability.
"""


def rand7():
    return random.randint(1, 7)


def rand5():
    num = rand7()

    while num == 6 or num == 7:
        num = rand7()

    return num


print('Rolling 5-sided die...')
print(rand5())
