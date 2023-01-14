
import numpy as np

def sieve(num : int) -> int:
    """Return largest prime divisor of num via Sieve of Eratosthenes"""
    upper_bound = round(np.sqrt(num + 1))
    divisors = [1] * upper_bound # 0 = not a prime divisor, 1 = prime divisor
    for divisor in range(2,upper_bound):
        if divisors[divisor] == 0:
            continue
        if num % divisor != 0:
            divisors[divisor] = 0
            continue
        if num % divisor == 0:
            divisors[divisor] = 1
            cur = 2 * divisor
            while(cur < upper_bound):
                divisors[cur] = 0
                cur += divisor
            continue

    max_prime_divisor = max(max(np.where(divisors)))
    return max_prime_divisor


if __name__ == "__main__":
    result = sieve(600851475143)
    print(result)


def test_basic():
    result = sieve(50)
    assert(result == 5)
    
def test_larger():
    result = sieve(1000)
    assert(result == 5)
    
def test_solution():
    result = sieve(600851475143)
    assert(result == 6857)