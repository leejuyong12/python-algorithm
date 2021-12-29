import sys
sys.stdin = open('촌수계산.txt')

def dfs(start):
    for s in graph[start]:
        if check[s] == 0:
            check[s] = check[start] + 1
            dfs(s)


n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for m in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)  # 무방향 그래프
    graph[y].append(x)
check = [0] * (n+1)
dfs(a)
if check[b] == 0:
    print(-1)
else:
    print(check[b])