import sys
sys.stdin = open('섬의 개수.txt')
sys.setrecursionlimit(5000000)      # 이거 써야한다
dx = [-1, 1, 0, 0, -1, 1, -1, 1] # dr
dy = [0, 0, -1, 1, -1, -1, 1, 1] # dc

def dfs(x,y):
    if 0 <= x < h and 0 <= y < w:
        if arr[x][y] == 1:
            arr[x][y] = 2
            dfs(x-1, y)
            dfs(x-1, y-1)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x+1, y-1)
            dfs(x+1, y+1)
            return True
        return False


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]

    cnt = 0
    for x in range(h):
        for y in range(w):
            if arr[x][y] == 1:
                dfs(x, y)
                cnt +=1
    print(cnt)

# bfs 코드
# from collections import deque
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     visited[x][y] = True
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < h and 0 <= ny < w:
#                 if graph[nx][ny] == 1 and not visited[nx][ny]:
#                     visited[nx][ny] = True
#                     queue.append((nx, ny))
#
# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]
#
# while True:
#     w, h = map(int, input().split())
#     if not w and not h:
#         break
#     graph = [list(map(int, input().split())) for _ in range(h)]
#     visited = [[False] * w for _ in range(h)]
#     cnt = 0
#
#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1 and not visited[i][j]:
#                 bfs(i, j)
#                 cnt += 1
#     print(cnt)