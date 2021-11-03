def check(x, y):
    global res
    arr[x][y] = 2
    res += 1
    for i in range(4):      # 0은 북, 1은 동, 2는 남, 3은 서
        nx = x + dx[i]
        ny = y + dy[i]
        if arr[nx][ny] == 0:
            check(x, y)


N, M = map(int, input())
r, c, d = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [list(map(int, input().split())) for _ in range(N)]
res = 0