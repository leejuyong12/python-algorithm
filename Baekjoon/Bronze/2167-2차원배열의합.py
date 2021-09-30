# 복습 필수

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

lst = [[0]*(M+1) for _ in range(N+1)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        lst[n][m] = arr[n - 1][m - 1] + lst[n][m - 1] + lst[n - 1][m] - lst[n - 1][m - 1]

K = int(input())
for k in range(K):
    i, j, x, y = map(int, input().split())
    print(lst[x][y] - lst[i-1][y] - lst[x][j-1] + lst[i-1][j-1])