import sys
sys.stdin = open('나이트의 이동.txt')
from collections import deque
# 우우상, 우상상, 우우하, 우하하, 하하좌, 하좌좌, 좌좌상, 좌상상
dx = [2, 1, 2, 1, -1, -2, -2, -1] # 좌우
dy = [1, 2, -1, -2, -2, -1, 1, 2] # 상하

def bfs(x, y, goal_a, goal_b):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        if x == goal_a and y == goal_b:
            return arr[x][y] -1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] == True:
                continue
            else:
                if arr[nx][ny] == 0:
                    queue.append((nx, ny))
                    arr[nx][ny] = arr[x][y] + 1
TC = int(input())

# while TC:
for t in range(TC):
    N = int(input())
    now_a, now_b = map(int, input().split())
    goal_a, goal_b = map(int, input().split())

    arr = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    if now_a == goal_a and now_b == goal_b:
        print(0)
        # TC -= 1
        # continue
    else:
        ans = bfs(now_a, now_b, goal_a, goal_b)
        print(ans)
    # TC -= 1