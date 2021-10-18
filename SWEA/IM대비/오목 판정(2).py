import sys
sys.stdin = open('오목 판정.txt')

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def check(x, y):
    for i in range(8):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
            cnt += 1
            nx = nx + dx[i]
            ny = ny + dy[i]
        if cnt == 5:
            return True
    return False

def omok():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if check(i ,j):
                    return True
    return False

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    if omok():
        print('#{} {}'.format(tc, 'YES'))
    else:
        print('#{} {}'.format(tc, 'NO'))
