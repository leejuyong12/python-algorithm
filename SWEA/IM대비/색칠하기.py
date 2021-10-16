import sys
sys.stdin = open('색칠하기.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    base = [[0] * 10 for _ in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                base[x][y] += color
    cnt = 0
    for i in range(10):
        for j in range(10):
            if base[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(tc, cnt))