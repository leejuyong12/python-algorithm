import sys
sys.stdin = open('[반복문1] 숫자사각형4.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    base = [[0]* N for _ in range(N)]
    mul = 1
    num = 1
    for x in range(N):
        num = x+1
        for y in range(N):
            base[x][y] = num
            num += mul
        mul += 1

    print('#{}'.format(tc))
    for x in range(N):
        for y in range(N):
            print(base[x][y], end=' ')
        print()