import sys
sys.stdin = open('그림.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    answer = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny] == True:
                continue
            else:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    answer += 1
    return answer


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

cnt = 0
max_cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            max_cnt = max(max_cnt, bfs(i, j))
print(cnt)
print(max_cnt)