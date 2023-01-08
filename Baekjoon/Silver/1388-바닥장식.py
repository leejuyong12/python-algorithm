import sys
sys.stdin = open('1388-바닥장식.txt')

N, M = map(int, input().split())

arr = []
for _ in range(N):
    a = list(input())
    arr.append(a)
# 별거 없음  그냥 -나 | 찾고 그자리에 탐색했다고 방문처리 해주고, 좌 우 살피는 코드 넣고 좌나 우의 자리값 넣어서 - 나 |면 dfs 돌려주기
def dfs(x,y):
    if arr[x][y] == '-':
        arr[x][y] = 1 # 방문처리
        for y_1 in [1,-1]:    # 좌우탐색
            Y = y + y_1
            if (Y > 0 and Y < M) and arr[x][Y] == '-':
                dfs(x,Y)
    if arr[x][y] == '|':
        arr[x][y] = 1 # 방문처리
        for x_1 in [1,-1]:    # 상하탐색
            X = x + x_1
            if (X > 0 and X < N) and arr[X][y] == '|':
                dfs(X,y)

cnt = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] == '-' or arr[x][y] == '|':
            dfs(x,y)
            cnt += 1
print(cnt)
# DFS로 안푼거
# cnt = 0
# # 세로 췍
# for x in range(M):
#     a = ''
#     for y in range(N):
#         if arr[y][x] == '|':
#             if arr[y][x] != a:
#                 cnt += 1
#         a = arr[y][x]
# # 가로 췍
# for x in range(N):
#     a = ''
#     for y in range(M):
#         if arr[x][y] == '-':
#             if arr[x][y] != a:
#                 cnt += 1
#         a = arr[x][y]
# print(cnt)
