def can_weight_item(w: int, m: int) -> str:
    """
    Determines if an item with mass m can be weighed using weights of masses
    w^0, w^1, w^2, ..., w^100, where weights can be placed on both pans
    of a balance scale.

    The problem is equivalent to determining if m can be expressed as a sum
    sum(c_k * w^k) where each coefficient c_k belongs to the set {-1, 0, 1}.

    Args:
        w: The base integer for the weights (2 <= w <= 10^9).
        m: The mass of the item to be weighed (1 <= m <= 10^9).

    Returns:
        'YES' if the item can be weighed, 'NO' otherwise.
    """

    # We process m by considering its remainder modulo w at each step.
    # This effectively determines the coefficient for the current power of w (w^k).
    # The 'm' variable iteratively represents the remaining mass to be balanced,
    # effectively shifting to higher powers of w.
    
    while m > 0:
        remainder = m % w
        
        if remainder == 0:
            # If m % w == 0, we can choose c_k = 0 for the current power w^k.
            # This means we don't use the weight w^k.
            # The remaining mass to represent for higher powers of w is m / w.
            m //= w
        elif remainder == 1:
            # If m % w == 1, we can choose c_k = 1 for the current power w^k.
            # This means we place the weight w^k on the right pan.
            # The remaining mass to represent is (m - 1) / w.
            m = (m - 1) // w
        elif remainder == w - 1:
            # If m % w == w - 1, this is equivalent to m % w == -1.
            # We can choose c_k = -1 for the current power w^k.
            # This means we place the weight w^k on the left pan (with the item).
            # The remaining mass to represent is (m + 1) / w.
            m = (m + 1) // w
        else:
            # If the remainder is anything else (not 0, 1, or w-1),
            # it's impossible to find a valid coefficient c_k in {-1, 0, 1}
            # that satisfies the congruence. Therefore, the item cannot be weighed.
            return 'NO'
            
    # If the loop completes, it means m has successfully been reduced to 0,
    # indicating that a valid representation with coefficients in {-1, 0, 1}
    # has been found.
    return 'YES'