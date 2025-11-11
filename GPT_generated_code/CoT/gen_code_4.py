def find_order(x, m):
    # We are looking for the smallest k such that x^k ≡ 1 (mod m)
    current = x % m
    k = 1
    while current != 1:
        current = (current * x) % m
        k += 1
    return k

def minimum_traps(m, x):
    return find_order(x, m)