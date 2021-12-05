import sys
sys.stdin = open('연결요소의개수.txt')
sys.setrecursionlimit(10000)
def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    # u, v = map(int, input().split()) # 이거 대신에
    u, v = map(int, sys.stdin.readline().strip().split()) # 이거 쓰니까 바로 시간초과 안뜬다.
    graph[u].append(v)
    graph[v].append(u)

# 이 밑부분 다시보기
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)