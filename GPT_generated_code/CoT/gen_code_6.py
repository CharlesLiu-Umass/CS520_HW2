def check_sequence(a, b, c):
    if c == 0:
        # If c is 0, the sequence is constant and only equal to a.
        if a == b:
            return "YES"
        else:
            return "NO"
    else:
        # Check if (b - a) is divisible by c and if the resulting index is valid (non-negative).
        if (b - a) % c == 0 and (b - a) // c >= 0:
            return "YES"
        else:
            return "NO"
