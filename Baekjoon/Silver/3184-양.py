import sys
sys.stdin = open('양.txt')
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    global s, w
    queue = deque()
    queue.append((x,y))
    ns = 0
    nw = 0
    visited[x][y] = True
    if arr[x][y] == 'o':
        ns += 1
    elif arr[x][y] == 'v':
        nw += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= R or nx < 0 or ny >= C or ny < 0 or arr[nx][ny] == '#':
                continue
            else:
                if arr[nx][ny] == 'o':
                    ns += 1
                elif arr[nx][ny] == 'v':
                    nw += 1
                visited[nx][ny] = True
                queue.append((nx,ny))
    if ns and nw:
        if ns > nw:
            w -= nw
        else:
            s -= ns




R, C = map(int, input().split())
arr = [list(input()) for _ in range(C)]
visited = [[False] * R for _ in range(C)]
s = 0
w = 0
for i in range(R):
    for j in range(C):
        if visited[i][j] == False:
            if arr[i][j] == 'o':
                s += 1
                visited[i][j] = True
            elif arr[i][j] == 'v':
                w += 1
                visited[i][j] = True
        bfs(i, j)
print(s, w)
