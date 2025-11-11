from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    >>> has_close_elements([], 0.1)
    False
    >>> has_close_elements([5.0], 0.1)
    False
    >>> has_close_elements([5.0, 5.0], 0.001)
    True
    >>> has_close_elements([5.0, 5.1], 0.1)
    False
    """
    # Step 1: Handle edge cases. If there are less than 2 numbers,
    # no two numbers can be compared.
    if len(numbers) < 2:
        return False

    # Step 2: Sort the list of numbers.
    # This is crucial because if two numbers are closer than the threshold,
    # they must be adjacent in the sorted list.
    sorted_numbers = sorted(numbers)

    # Step 3: Iterate through the sorted list, comparing adjacent elements.
    # We only need to go up to the second-to-last element (index len-2)
    # because we compare numbers[i] with numbers[i+1].
    for i in range(len(sorted_numbers) - 1):
        # Step 4: Calculate the absolute difference between the current number
        # and the next number in the sorted list.
        diff = abs(sorted_numbers[i+1] - sorted_numbers[i])

        # Step 5: Check if this difference is less than the given threshold.
        # If it is, we immediately found a pair satisfying the condition,
        # so we can return True.
        if diff < threshold:
            return True

    # If the loop completes without finding any such pair, it means
    # no two numbers in the list are closer than the threshold.
    return False