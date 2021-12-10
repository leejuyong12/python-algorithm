import sys
sys.stdin = open('안전영역.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, safe):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > safe and visited[nx][ny] == False: # = 빼니까 맞다
                    visited[nx][ny] = True
                    queue.append((nx, ny))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_safe = max(map(max, arr))   # arr 에서 최대값 찾는 빠른 방법
res = 0
for safe in range(max_safe):    # 빗물 깊이가 작은곳부터 큰곳까지 비교해서 안전한 영역 최대 찾기
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > safe and visited[i][j] == False: # = 빼니까 맞다
                bfs(i, j, safe)
                cnt += 1
    if res < cnt:       # 빗물을 제일 작은 곳부터 비교하니까
        res = cnt       # 최댓값 구하는 코드 작성
print(res)

# import sys
# sys.setrecursionlimit(10000)
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def dfs(x, y, h):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if(0 <= nx < N) and (0 <= ny < N):
#             if arr[nx][ny] > h and done[nx][ny] == 0:
#                 done[nx][ny] = 1
#                 dfs(nx, ny, h)
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# for k in range(max(map(max, arr))): # 주어진 배열에서 가장 큰값만큼 반복
#     # 매번 초기화
#     cnt = 0
#     done = [[0]*N for _ in range(N)]
#     # 입력 받은 arr배열 탐색
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > k and done[i][j] == 0:
#                 done[i][j] = 1
#                 cnt += 1
#                 dfs(i, j, k)
#     ans = max(ans, cnt)
# print(ans)

