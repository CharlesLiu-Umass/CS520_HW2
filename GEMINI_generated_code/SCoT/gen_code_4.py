import math

# Function to find prime factors of a number n
# Returns a list of prime factors, e.g., prime_factorize(12) -> [2, 2, 3]
def prime_factorize(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

# Function to get distinct prime factors and their counts
# Returns a dictionary, e.g., {2: 2, 3: 1} for 12
def get_prime_factor_counts(n):
    factors = prime_factorize(n)
    counts = {}
    for f in factors:
        counts[f] = counts.get(f, 0) + 1
    return counts

# Function for modular exponentiation (base^exp % mod)
def mod_pow(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

# Function to calculate Euler's totient function phi(n)
# Needs factor_counts_n (a dict of prime factors and their counts) for n
def calculate_phi(n, factor_counts_n):
    if n == 0: return 0
    if n == 1: return 1
    result = n
    for p in factor_counts_n:
        result -= result // p
    return result

# Function to calculate the multiplicative order of 'base' modulo 'mod'
# phi_val is phi(mod)
# global_phi_prime_factors is a precomputed list of all possible prime factors of any phi(m')
def get_order(base, mod, phi_val, global_phi_prime_factors):
    if mod == 1: return 1 
    
    order = phi_val
    for p in global_phi_prime_factors:
        # If p is a factor of the current 'order' candidate
        # And if x^(order/p) mod mod is 1, then we can reduce the order by dividing by p
        if order % p == 0:
            while order % p == 0 and mod_pow(base, order // p, mod) == 1:
                order //= p
    return order

def solve(m, x):

    # Step 1: Add 1 trap for room 0
    total_traps = 1

    # Step 2: Get prime factorization of m
    factor_counts_m = get_prime_factor_counts(m)
    distinct_prime_factors_m = list(factor_counts_m.keys())

    # Step 3: Collect all possible prime factors that might appear in phi(n') for any n' which is a divisor of m.
    # This set will be used to optimize order calculation.
    # Prime factors of phi(N) are p_i (prime factors of N) and prime factors of (p_i - 1).
    global_phi_prime_factors = set()
    for p in distinct_prime_factors_m:
        if p > 1:
            global_phi_prime_factors.add(p) 
            factors_p_minus_1 = prime_factorize(p - 1)
            for fp in factors_p_minus_1:
                global_phi_prime_factors.add(fp)
    global_phi_prime_factors = list(global_phi_prime_factors) 

    # Step 4: Iterate through all divisors 'd' of 'm' (except m itself)
    divisors = set()
    
    # Recursive function to generate all divisors of m
    def generate_divisors(idx, current_divisor):
        if idx == len(distinct_prime_factors_m):
            divisors.add(current_divisor)
            return

        p = distinct_prime_factors_m[idx]
        max_exp = factor_counts_m[p]
        
        power_p = 1
        for _ in range(max_exp + 1):
            generate_divisors(idx + 1, current_divisor * power_p)
            power_p *= p
    
    generate_divisors(0, 1)

    for d in divisors:
        if d == m: 
            continue # d=m corresponds to m'=1. The set of rooms {i | GCD(i,m)=m, i in {1..m-1}} is empty.

        m_prime = m // d
        
        # Calculate prime factors of m_prime based on prime factors of m
        current_factor_counts_m_prime = {}
        temp_d = d
        factor_counts_d = {}
        for p in distinct_prime_factors_m:
            count = 0
            while temp_d % p == 0:
                count += 1
                temp_d //= p
            if count > 0:
                factor_counts_d[p] = count
        
        for p in distinct_prime_factors_m:
            exp_in_m = factor_counts_m[p]
            exp_in_d = factor_counts_d.get(p, 0)
            if exp_in_m - exp_in_d > 0:
                current_factor_counts_m_prime[p] = exp_in_m - exp_in_d
            
        phi_m_prime = calculate_phi(m_prime, current_factor_counts_m_prime)
        
        if phi_m_prime == 0: # Should only happen if m_prime = 0, which is not possible here
            continue
        
        order_x = get_order(x, m_prime, phi_m_prime, global_phi_prime_factors)
        
        # The number of cycles for this d (and corresponding m') is phi(m') / order(x)
        total_traps += phi_m_prime // order_x

    return total_traps