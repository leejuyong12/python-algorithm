import sys
sys.stdin = open('상근이의 여행.txt')
sys.setrecursionlimit(100000)      # 이거 써야한다

def dfs(start):
    global cnt
    visited[start] = 1
    for i in tree[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
    return cnt
T = int(input())
for t in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    tree = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0
    for i in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        tree[a].append(b)
        tree[b].append(a)
    result = dfs(1)
    print(result)