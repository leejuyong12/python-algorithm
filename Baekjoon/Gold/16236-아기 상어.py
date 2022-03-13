import sys
sys.stdin = open('아기상어.txt')
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= 0 or nx > N or ny <= 0 or ny > N:
                continue
            
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]