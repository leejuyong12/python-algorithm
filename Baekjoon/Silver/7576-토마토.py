import sys
sys.stdin = open('토마토.txt')
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([])
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for a in range(N):
    for b in range(M):
        if arr[a][b] == 1:
            queue.append([a,b])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    queue.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1
bfs()
isTrue = False
result = -2
for i in arr:
    for j in i:
        if j == 0:
            isTrue = True       # 0이 하나라도 있다면
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
# answer = 0
# for i in arr:
#     for j in i:
#         if j == 0:
#             print(-1)
#     answer = max(answer, max(i))
# print(answer-1)