import math

def prime_factorize(n):
    """
    Returns a list of (prime, exponent) tuples for the prime factorization of n.
    Handles n=0 and n=1 by returning empty list.
    """
    factors = []
    if n <= 1:
        return factors
    
    d = 2
    temp_n = n
    while d * d <= temp_n:
        if temp_n % d == 0:
            count = 0
            while temp_n % d == 0:
                temp_n //= d
                count += 1
            factors.append((d, count))
        d += 1
    if temp_n > 1:
        factors.append((temp_n, 1))
    return factors

def get_divisors_recursive(prime_factors_with_exp):
    """
    Generates all divisors of a number given its prime factorization.
    """
    divs = []
    
    def generate(idx, current_divisor):
        if idx == len(prime_factors_with_exp):
            divs.append(current_divisor)
            return
        
        p, a = prime_factors_with_exp[idx]
        power_p = 1
        for _ in range(a + 1): # Iterate through 0 to 'a' for exponent of p
            generate(idx + 1, current_divisor * power_p)
            power_p *= p
            
    generate(0, 1)
    return sorted(divs)

def power(base, exp, mod):
    """
    Performs modular exponentiation (base^exp % mod).
    """
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def minimum_traps(m, x):
    """
    Calculates the minimum number of traps required to catch the x-mouse.
    
    Args:
        m (int): The number of rooms (2 <= m <= 10^14).
        x (int): The x-mouse parameter (1 <= x < m, GCD(x, m) = 1).
        
    Returns:
        int: The minimum number of traps.
    """
    total_traps_count = 1 # For room 0

    m_prime_factors_with_exp = prime_factorize(m)
    
    # Precompute prime factors of (P-1) for each distinct prime P in m_prime_factors_with_exp.
    # This optimizes the calculation of prime factors of phi(N) later.
    prime_factors_of_P_minus_1_cache = {}
    for p, _ in m_prime_factors_with_exp:
        # p is a prime, so p >= 2. p-1 >= 1. prime_factorize(1) returns [].
        prime_factors_of_P_minus_1_cache[p] = prime_factorize(p - 1)
    
    divisors = get_divisors_recursive(m_prime_factors_with_exp)

    for g in divisors:
        if g == m: 
            continue # Exclude g=m, as N=m/g=1 for which order is not standard (or refers to room 0 cycle)
        
        N = m // g
        
        # Determine prime factors of N and distinct primes of N based on m's factorization.
        N_prime_factors_with_exp = []
        distinct_primes_of_N = []
        
        current_N_val = N # Use a temporary variable to find exponents without altering original N
        for p_m, a_m in m_prime_factors_with_exp:
            if current_N_val % p_m == 0: # If p_m is a prime factor of N
                count_N = 0
                while current_N_val > 0 and current_N_val % p_m == 0:
                    count_N += 1
                    current_N_val //= p_m
                N_prime_factors_with_exp.append((p_m, count_N))
                distinct_primes_of_N.append(p_m)

        # Calculate phi(N) using N and its distinct prime factors
        phi_N = N
        for p in distinct_primes_of_N:
            phi_N -= phi_N // p
        
        # Calculate distinct prime factors of phi(N) to efficiently find the order
        phi_N_distinct_prime_factors_for_order = set()
        for p_N, b_N in N_prime_factors_with_exp:
            if b_N > 0: # Prime factor p_N must be present in N (i.e., b_N >= 1)
                # The term p_N^(b_N-1) in phi(N) contributes p_N as a prime factor
                phi_N_distinct_prime_factors_for_order.add(p_N)
                # The term (p_N-1) contributes its prime factors (from precomputed cache)
                for q, _ in prime_factors_of_P_minus_1_cache[p_N]:
                    phi_N_distinct_prime_factors_for_order.add(q)
        
        # Calculate ord_N(x)
        order = phi_N
        if phi_N <= 1: # If phi_N is 0 or 1, the order is 1 (e.g., N=2, phi(2)=1).
            order = 1
        else:
            # Iterate through distinct prime factors of phi_N to reduce the order
            for p_factor in sorted(list(phi_N_distinct_prime_factors_for_order)):
                while order % p_factor == 0 and power(x, order // p_factor, N) == 1:
                    order //= p_factor
        
        total_traps_count += phi_N // order
        
    return total_traps_count