import sys
sys.stdin = open('14940-쉬운 최단거리.txt')
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 상 하 좌 우
dx = [-1, 1, 0, 0] # 세로
dy = [0, 0, -1, 1]  # 가로
visited = [[-1]*m for _ in range(n)]
def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            print(0, end = " ")
        else:
            print(visited[x][y], end = " ")
    print()

