"""
Write a function that calculates how many squares of rain would be captured for 
a set of building heights.
"""

def rain(lst):
    """Calculate collected rainwater between buildings."""
    collected_rain = 0

    for i, height in enumerate(lst):
        left_tallest = max(lst[:(i + 1)])
        right_tallest = max(lst[i:]) 
        leak_height = min(right_tallest, left_tallest)
        collected_rain += leak_height - height

    return collected_rain


print rain([3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])