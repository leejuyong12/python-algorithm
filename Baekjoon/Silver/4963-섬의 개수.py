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