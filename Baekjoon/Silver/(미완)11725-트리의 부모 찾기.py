import sys
sys.stdin = open('트리의 부모 찾기.txt')

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for n in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(V):
    visited[V] = True
    for i in tree[V]:
        if not visited[i]:
            dfs(i)
dfs(1)
for i in tree[2:]:
  print(i[0])