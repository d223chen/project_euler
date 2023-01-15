


def solve(n : int) -> int:
    # prime number theorem states that number of primes less than n is ~ n/ln(n)
    # therefore, the nth prime number is upper bounded by ~ n^2
    array = [True] * n * n
    count = 0
    for num in range(2, len(array)):
        if array[num]:
            count += 1
            if count == n:
                return num
            cur = num * 2
            while (cur < len(array)):
                array[cur] = False
                cur += num

    

if __name__ == "__main__":
    result = solve(10001)
    print(result)
    
def test_basic():
    result = solve(1)
    assert(result == 2)
    
def test_small():
    result = solve(2)
    assert(result == 3)
    
def test_medium():
    result = solve(3)
    assert(result == 5)
    
def test_medium2():
    result = solve(4)
    assert(result == 7)
    
def test_six():
    result = solve(6)
    assert(result == 13)