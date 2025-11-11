def can_balance(w, m):
    while m != 0:
        remainder = m % w
        
        if remainder == 0:
            # No weight needed for this power of w.
            m //= w
        elif remainder == 1:
            # Put weight on the right pan for this power of w.
            m -= 1
            m //= w
        elif remainder == w - 1:
            # Put weight on the left pan for this power of w.
            m += 1
            m //= w
        else:
            # If remainder is not 0, 1 or w-1, it's impossible to balance.
            return "NO"
    
    return "YES"
