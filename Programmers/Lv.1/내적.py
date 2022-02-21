def solution(a, b):
    ans = 0
    for x in range(len(a)):
        ans += a[x] * b[x]
    return ans
