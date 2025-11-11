def check_sequence_element(a: int, b: int, c: int) -> str:
    """
    Checks if an integer 'b' appears in an arithmetic sequence 's'
    where s_1 = a and s_i - s_{i-1} = c.

    Args:
        a (int): The first element of the sequence.
        b (int): Vasya's favorite number to check.
        c (int): The common difference between neighboring elements.

    Returns:
        str: "YES" if b appears in the sequence, "NO" otherwise.
    """
    if c == 0:
        # If the common difference is 0, the sequence is a, a, a, ...
        # So b is in the sequence if and only if b is equal to a.
        return "YES" if a == b else "NO"
    else:
        # If c is not 0, we are looking for a non-negative integer k (k = i-1 >= 0)
        # such that b = a + k * c.
        # This implies: (b - a) = k * c.

        diff = b - a

        # Condition 1: (b - a) must be perfectly divisible by c.
        # This is checked by (diff % c == 0).
        # Condition 2: k = (b - a) / c must be non-negative.
        # This is checked by (diff // c) >= 0 using floor division.
        # Python's % operator returns a result with the same sign as the divisor (c),
        # so diff % c == 0 correctly checks for divisibility regardless of signs.
        # Python's // operator performs floor division, ensuring that
        # (diff // c) >= 0 correctly implies that diff and c have consistent signs
        # (or diff is zero), which is necessary for k >= 0.

        if diff % c == 0 and (diff // c) >= 0:
            return "YES"
        else:
            return "NO"