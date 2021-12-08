import sys
sys.stdin = open('단지번호붙이기.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):

    global cnt
    if 0 <= x < N and 0 <= y < N:
        if arr[x][y] == 1:
            cnt += 1
            arr[x][y] = 0   # 센거는 0으로 바꾸기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
        return False



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0  # 각 블록당 몇개냐
res = 0  # 몇 개의 블록이 나오느냐
result = [] # 밑에서 순서대로 출력하기 위해 리스트로 생성
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result.append(cnt)
            res += 1
            cnt = 0

result.sort()
print(res)
for a in result:
    print(a)

# bfs 로 풀기
# from collections import deque
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# def bfs(graph, a, b):
#     n = len(graph)
#     queue = deque()
#     queue.append((a, b))
#     graph[a][b] = 0
#     count = 1
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))
#                 count += 1
#     return count
#
#
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# cnt = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             cnt.append(bfs(graph, i, j))
#
# cnt.sort()
# print(len(cnt))
# for i in range(len(cnt)):
#     print(cnt[i])