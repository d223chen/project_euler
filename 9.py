
def solve(sum : int) -> int:
    for a in range(1, sum):
        for b in range(a+1,sum):
            c = sum - b - a
            if a**2 + b**2 == c**2:
                return a*b*c
                

if __name__ == "__main__":
    result = solve(1000)
    print(result)
    
def test_basic():
    result = solve(12)
    assert(result == 3 * 4 * 5)