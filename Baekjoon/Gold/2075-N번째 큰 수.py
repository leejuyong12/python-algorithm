import sys
sys.stdin = open('N번째큰수.txt')
import heapq
# 처음에 풀때는 bfs인줄 알았는데, heapq라는 것을 사용해서 푸는 문제였다.
# 모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리(binary tree) 구조인데,
# 내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태로 정렬된다.
h = []
N = int(sys.stdin.readline())
for n in map(int, sys.stdin.readline().split()):
    heapq.heappush(h, n)
for _ in range(1, N):
    for n in map(int, sys.stdin.readline().split()):
        heapq.heappush(h, n)    # h 리스트에
        heapq.heappop(h)        # 가장 작은 원소 빼내기
print(heapq.heappop(h))

# from collections import deque
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#     visited[x][y] = True
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if visited[nx][ny] == False:
#                     visited[nx][ny] = True
#                     queue.append((nx, ny))
#
# N = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# cnt = 0
# base = arr[0][0]
# for x in range(N):
#     for y in range(N):
#         if arr[x][y] < base:
#             base = arr[x][y]
# visited = [False] * N
# for x in range(N):
#     for y in range(N):
#         if arr[x][y]


