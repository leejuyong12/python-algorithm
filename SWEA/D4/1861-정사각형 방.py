import sys
sys.stdin = open('정사각형방.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    global max_cnt, min_start, cnt, start

    if cnt > max_cnt:
        max_cnt = cnt
        min_start = start

    if max_cnt == cnt:
        if min_start > start:
            min_start = start

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if A[nx][ny] - A[x][y] == 1:
            cnt += 1
            check(nx, ny)
            cnt -= 1

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    min_start = 987654321
    cnt = 1
    start = 0

    for i in range(N):
        for j in range(N):
            start = A[i][j]
            check(i, j)
    print('#{} {} {}'.format(tc, min_start, max_cnt))



