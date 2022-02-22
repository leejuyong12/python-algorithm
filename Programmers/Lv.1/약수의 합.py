def solution(n):
    ans = 0
    for x in range(1, n+1):
        if n % x == 0:
            ans += x
    return ans