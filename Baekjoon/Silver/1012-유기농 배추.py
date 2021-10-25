import sys
sys.stdin = open('유기농 배추.txt')
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(c, r):
    queue = deque()
    queue.append((c,r))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx,ny))

TC = int(input())
for tc in range(1, TC+1):
    N, M, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    visited = [[0] * K for _ in range(K)]
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1:
                bfs(x,y)
                cnt += 1
    print(cnt)


