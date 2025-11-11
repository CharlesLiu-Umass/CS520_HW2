def minimum_operations(n, s):
    # Step 1: Initialize the minimum number of operations to n (typing each character individually)
    min_ops = n
    
    # Step 2: Check all possible lengths of prefix from 1 to n
    for k in range(1, n):
        # If the first k characters can be repeated in the next k characters
        if s[:k] == s[k:k+k]:
            # If we can copy, we calculate the number of operations
            # Operations = typing k characters + 1 copy operation + (remaining characters to type)
            min_ops = min(min_ops, k + 1 + (n - 2 * k))
    
    return min_ops
