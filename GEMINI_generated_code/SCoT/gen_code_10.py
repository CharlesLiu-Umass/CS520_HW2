def solve(w, m):

    current_m = m

    while current_m > 0:
        remainder = current_m % w

        if remainder == 0:
            # If current_m is a multiple of w, we don't need to use the current power of w.
            # This corresponds to choosing c_k = 0.
            current_m //= w
        elif remainder == 1:
            # If current_m % w is 1, we put w^k on the right pan.
            # This corresponds to choosing c_k = 1.
            # The remaining mass (m - w^k) must be a multiple of w.
            # (current_m - 1) // w effectively transitions to the next power of w.
            # For example, if current_m = q*w + 1, then (current_m - 1) // w = q.
            # Integer division current_m // w also yields q in this case.
            current_m //= w 
        elif remainder == w - 1:
            # If current_m % w is w-1, we put w^k on the left pan.
            # This corresponds to choosing c_k = -1.
            # The remaining mass (m + w^k) must be a multiple of w.
            # (current_m + 1) // w effectively transitions to the next power of w.
            # For example, if current_m = q*w + (w-1), then (current_m + 1) // w = (q*w + w) // w = q + 1.
            current_m = (current_m + 1) // w
        else:
            # If remainder is any other value (2, 3, ..., w-2),
            # it's impossible to balance using c_k in {-1, 0, 1}.
            return "NO"

    # If current_m becomes 0, it means we successfully balanced all parts of m.
    return "YES"