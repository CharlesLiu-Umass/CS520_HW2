def can_weight(w, m):
    while m != 0:
        remainder = m % w
        
        if remainder == 0:
            m //= w  # No weight needed at this level
        elif remainder == 1:
            m //= w  # Use the weight on the right pan
        elif remainder == w - 1:
            m = (m + 1) // w  # Use the weight on the left pan, and adjust m
        else:
            return "NO"
    
    return "YES"
