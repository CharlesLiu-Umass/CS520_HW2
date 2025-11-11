from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two elements are closer than threshold."""
    numbers.sort()  # Sort the list
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True
    return False