import sys
sys.stdin = open('기지국.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        for j in range(ord(arr[x][y])-65+1):
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                arr[nx][ny] = 'X'
            nx = nx + dx[i]
            ny = ny + dy[i]

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                check(i, j)
    res = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                res += 1
    print('#{} {}'.format(tc, res))