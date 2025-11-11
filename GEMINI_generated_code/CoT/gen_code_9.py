def min_typing_operations(n: int, s: str) -> int:
    """
    Calculates the minimum number of operations to type a given string.

    Args:
        n: The length of the string s.
        s: The string consisting of n lowercase Latin letters.

    Returns:
        The minimum number of operations needed to type the string.
    """
    # Initialize minimum operations assuming we type all characters one by one.
    min_operations = n

    # Iterate through all possible lengths 'k' for the initial string
    # that is typed before a potential copy operation.
    # The copied string will have length 2*k.
    # For a copy to be useful, 2*k must not exceed the target string length 'n'.
    # So, 'k' can range from 1 up to n // 2 (inclusive).
    for k in range(1, n // 2 + 1):
        # Check if the prefix of length 'k' (s[0:k])
        # is identical to the substring from index 'k' to '2*k - 1' (s[k : 2*k]).
        # If this condition holds, it means we can form the prefix s[0...2k-1]
        # by typing s[0...k-1] and then copying it.
        if s[0:k] == s[k : 2 * k]:
            # If a match is found:
            # 1. Type 'k' characters: 'k' operations.
            # 2. Perform the copy operation: '1' operation.
            #    (Current string is now s[0...2k-1])
            # 3. Type the remaining characters one by one: 'n - 2*k' operations.
            # Total operations for this strategy: k + 1 + (n - 2*k) = n - k + 1.
            current_ops = n - k + 1
            
            # Update the overall minimum operations found so far.
            min_operations = min(min_operations, current_ops)
            
    return min_operations