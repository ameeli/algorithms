# Given a list of people and their birth and death years, find the year with
# the most number of people alive.


def find_most_populated_year(population):
    """
    Input ex: [(1763, 1819), (1956, 2000), (1892, 2000)]
    """
    # find min birth and max death years
    # create dict with comprehension with above years, value 0
    # loop through population
    # increment dict value by one
    # find key with highest value
