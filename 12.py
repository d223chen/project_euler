
def num_divisors(num : int) -> int:
    count = 0
    for divisor in range(1,num+1):
        if num % divisor == 0:
            count += 1

    return count

def solve(divisors: int) -> int:
    cur = 0
    for n in range(10000):
        cur += n
        
        if num_divisors(cur) >= divisors:
            return cur

if __name__ == "__main__":
    result = solve(500)
    print(result)
    
def test_basic():
    assert(solve(1) == 1)
    assert(solve(2) == 3)
    assert(solve(3) == 6)
    assert(solve(4) == 6)
    assert(solve(5) == 28)