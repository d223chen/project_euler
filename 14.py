


def solve(num: int) -> int:
    dp = dict()
    max_starter = 0
    max_length = 0
    for n in range(1, num): #strictly less than num
        cur = n
        length = 0
        early_stop = False
        while(cur != 1):
            if cur in dp.keys():
                dp[n] = length + dp[cur]
                early_stop = True
                break
            if cur % 2 == 0:
                cur = cur / 2
            else:
                cur = 3 * cur + 1
            length += 1
            
        if not early_stop:
            dp[n] = length
            
        if dp[n] > max_length:
            max_starter = n
            max_length = dp[n]
            
    return max_starter
        
if __name__ == "__main__":
    result = solve(1000000)
    print(result)
    
def test_basic():
    assert(solve(14)==9)
    assert(solve(100)==97)