def min_typing_operations(n: int, s: str) -> int:
    """
    Calculates the minimum number of operations to type the given string.

    Args:
        n: The length of the string.
        s: The string to be typed.

    Returns:
        The minimum number of operations.
    """
    
    # Initialize minimum operations with the cost of typing all characters one by one.
    min_ops = n

    # Iterate through all possible lengths 'k' for the prefix that could be copied.
    # 'k' must be at least 1.
    # When we copy a prefix of length 'k', the string becomes 2*k characters long.
    # This 2*k length must not exceed 'n' (the target string length).
    # So, k can go from 1 up to n // 2 (integer division).
    for k in range(1, n // 2 + 1):
        # Check if the first 'k' characters of 's' are identical
        # to the next 'k' characters (from index 'k' to '2k-1').
        if s[:k] == s[k : 2*k]:
            # If they are identical, we can use the copy operation.
            # The total operations for this 'k' would be:
            # 1. 'k' operations to type the initial prefix s[0...k-1].
            # 2. '1' operation to perform the copy (string becomes s[0...k-1]s[0...k-1]).
            # 3. 'n - 2*k' operations to type the remaining characters s[2k...n-1].
            # Total = k + 1 + (n - 2*k)
            # This simplifies to n - k + 1.
            
            current_ops = n - k + 1
            
            # Update the overall minimum operations found so far.
            min_ops = min(min_ops, current_ops)
            
    return min_ops