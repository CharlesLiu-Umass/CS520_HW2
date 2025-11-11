def is_b_in_sequence(a, b, c):
    # Case 1: If the common difference is 0, the sequence is constant with all terms equal to a.
    if c == 0:
        return "YES" if a == b else "NO"
    
    # Case 2: If c is non-zero, check if (b - a) is divisible by c and if the index i is positive
    if (b - a) % c == 0 and (b - a) // c >= 0:
        return "YES"
    else:
        return "NO"