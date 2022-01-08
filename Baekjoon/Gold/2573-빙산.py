import sys
sys.stdin = open('빙산.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == 0:
                    count_0[x][y] += 1

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

check = False
day = 0
while True:
    visited = [[False] * M for _ in range(N)]
    count_0 = [[0] * M for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and visited[i][j] == False:
                bfs(i,j)
                result += 1
    for i in range(N):
        for j in range(M):
            graph[i][j] -= count_0[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if result == 0:
        break
    if result >= 2:
        check = True
        break
    day += 1
if check:
    print(day)
else:
    print(0)