import sys
sys.stdin = open('미로탐색.txt')
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    cnt = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                cnt += 1
                queue.append((nx,ny))
    return cnt
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]

print(bfs(0,0))