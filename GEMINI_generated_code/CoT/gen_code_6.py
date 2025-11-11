def check_vasyas_sequence(a: int, b: int, c: int) -> str:
    """
    Checks if Vasya's favorite integer 'b' appears in a sequence 's'.

    The sequence s is an arithmetic progression:
    s_1 = a
    s_i - s_{i-1} = c

    Args:
        a (int): The first element of the sequence.
        b (int): Vasya's favorite number.
        c (int): The common difference between elements.

    Returns:
        str: "YES" if b appears in the sequence, "NO" otherwise.
    """
    if c == 0:
        # If the common difference is 0, the sequence is a, a, a, ...
        # So b is in the sequence if and only if b is equal to a.
        if a == b:
            return "YES"
        else:
            return "NO"
    else:
        # If the common difference is not 0, we're looking for an integer i >= 1 such that:
        # b = a + (i - 1) * c
        # Rearranging: (b - a) = (i - 1) * c

        # Calculate the difference between b and a.
        difference = b - a

        # Condition 1: (b - a) must be divisible by c.
        # If not, (i - 1) would not be an integer.
        if difference % c != 0:
            return "NO"

        # Condition 2: The calculated (i - 1) must be non-negative.
        # i - 1 = (b - a) / c
        # Let k = (b - a) / c. We need k >= 0 for i = k + 1 to be >= 1.
        k = difference // c # Use integer division

        if k >= 0:
            return "YES"
        else:
            # If k < 0, it means i-1 < 0, so i < 1.
            # But the problem requires i to be a positive integer (i >= 1).
            return "NO"