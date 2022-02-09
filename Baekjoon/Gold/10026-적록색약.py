import sys
sys.stdin = open('적록색약.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] == True:
                continue
            else:
                if arr[nx][ny] == arr[x][y]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

N = int(input())

arr = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt_a = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            cnt_a += 1
visited = [[False] * N for _ in range(N)]
cnt_b = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            cnt_b+= 1
print(cnt_a, cnt_b)