def check(a, b):
    lst = '0123456789ABCDEF'
    x, y = divmod(a, b)
    if x == 0:
        return lst[y]
    else:
        return check(x, b) + lst[y]

def solution(n, t, m, p):
    ans = ''    # 전체 말하는 숫자
    res = ''    # 그중에 구해야할 숫자
    for x in range(m*t):
        ans += str(check(x, n))
    while len(res) < t:
        res += ans[p-1]
        p += m
    return res