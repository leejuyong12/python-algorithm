import sys
sys.stdin = open('최장 경로.txt')


def dfs(a, cnt):
    global ans

    if ans < cnt:
        ans = cnt
    visited[a] = True
    for x in arr[a]:
        if visited[x] == 0:
            dfs(x, cnt + 1)
            visited[x] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]

    for i in range(M):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)

    ans = 0
    for j in range(1, N + 1):
        visited = [0] * (N + 1)
        dfs(j, 1)

    print('#{} {}'.format(tc, ans))