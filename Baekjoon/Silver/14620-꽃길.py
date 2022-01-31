import sys
sys.stdin = open('꽃길.txt')

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def dfs(x, y, N):
    result = 0
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N and 0 <= ny < N) or visited[nx][ny] == False:
            result += flowers[nx][ny]
            return True
    return False



N = int(input())
flowers = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = 0
