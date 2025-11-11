from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference between the two numbers
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False