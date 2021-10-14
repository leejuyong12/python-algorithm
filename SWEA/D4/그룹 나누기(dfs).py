import sys
sys.stdin = open('그룹 나누기.txt')

def dfs(curV):
    visited[curV] = True

    for newV in G[curV]:
        if not visited[newV]:
            dfs(newV)

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    G = [[] for _ in range(N+1)]

    for i in range(M):
        s1 = lst[i*2]
        s2 = lst[i*2+1]
        G[s1].append(s2)
        G[s2].append(s1)

    cnt = 0
    visited = [False] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print('#{} {}'.format(tc, cnt))