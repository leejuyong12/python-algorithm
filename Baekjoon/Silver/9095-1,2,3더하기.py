import sys
sys.stdin = open('123더하기.txt')

# 1일때 1, 2일때 2, 3일때 4, 4일때 7, 5일때 13
TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    res = [0] * (n+1)

    # res[1] = 1        # 이렇게 했는데 런타임에러
    # res[2] = 2        # why?
    # res[3] = 4
    res[1] = 1
    if n > 1:
        res[2] = 2
        if n > 2:
            res[3] = 4
    if n > 3:
        for i in range(4, n+1):
            res[i] = res[i-1] + res[i-2] + res[i-3]

    print(res[n])
