import sys
sys.stdin = open('오목 판정.txt')

dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

def check(r, c):

    for i in range(8):
        cnt = 1
        nr = r + dr[i]
        nc = c + dc[i]
        while 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 'o':
            cnt += 1
            nr = nr + dr[i]
            nc = nc + dc[i]
        if cnt == 5:
            return True
    return False

def omok():
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 'o':
                if check(i, j):
                    return True
    return False

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]

    if omok():
        print('#{} {}'.format(tc, 'YES'))
    else:
        print('#{} {}'.format(tc, 'NO'))