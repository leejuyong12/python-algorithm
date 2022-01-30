import sys
sys.stdin = open('특정 거리의 도시 찾기.txt')
from collections import deque
def bfs(start):
    answer = []
    visited[start] = True
    queue = deque([start])
    print(queue)
    while queue:
        X = queue.popleft()
        for i in arr[X]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[X] + 1
                if distance[i] == K:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for a in answer:
            print(a)


N, M, K, X = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
distance = [0] * (N+1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split()) # 단방향
    arr[A].append(B)
visited = [False] * (N+1)
bfs(X)