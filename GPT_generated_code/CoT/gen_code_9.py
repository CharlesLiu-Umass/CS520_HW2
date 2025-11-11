def min_operations(n, s):
    # The minimum operations is initially typing each character individually
    min_ops = n
    
    # Try every possible length of the prefix that might be copied
    for k in range(1, n):
        if s[:k] == s[k:2*k]:  # Check if the first 'k' characters can be repeated
            # Operations: k for typing the first k characters, 1 for the copy, and remaining (n - 2*k)
            min_ops = min(min_ops, k + 1 + (n - 2*k))
    
    return min_ops
