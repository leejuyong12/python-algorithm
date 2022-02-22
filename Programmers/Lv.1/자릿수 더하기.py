def solution(n):
    lst = list(str(n))
    ans = 0
    for x in lst:
        ans += int(x)
    return ans