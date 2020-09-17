import random

"""
Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have
the same probability of ending up in each spot in the final list.
"""


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    for i in range(len(the_list)):
        new_idx = get_random(i, len(the_list) - 1)

        if i != new_idx:
            the_list[i], the_list[new_idx] = the_list[new_idx], the_list[i]


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
