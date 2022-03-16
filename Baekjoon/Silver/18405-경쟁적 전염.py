import sys
sys.stdin = open('경쟁적 전염.txt')
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 1 2 3 1 2 3 이렇게 순차적으로 하는 방법이 뭐가있을까
def bfs(S, x,y):
    cnt = 0
    queue = deque(virus)
    while queue:
        if cnt == S:
            break
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            else:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y]
                    queue.append((nx, ny))
    cnt += 1
    return arr[x][y]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())  # X 랑 Y  -1 하기
visited = [[False] * N for _ in range(N)]
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            virus.append( (arr[i][j])
virus.sort()

# print(bfs(S, X-1, Y-1))

