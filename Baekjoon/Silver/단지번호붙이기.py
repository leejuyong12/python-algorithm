import sys
sys.stdin = open('단지번호붙이기.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    c = 0
    if arr[x][y] == 1:
        arr[x][y] += c
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:

                dfs(nx, ny)


N = int(input())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
