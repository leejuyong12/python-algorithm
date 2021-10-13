import sys
sys.stdin = open('최장 경로.txt')


def dfs(ni, cnt):
    global ans

    if ans < cnt:
        ans = cnt

    for pi in range(1, N + 1):
        if adj[ni][pi] and visited[pi] == 0:
            visited[pi] = 1
            dfs(pi, cnt + 1)
            visited[pi] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for k in range(M):
        adj[arr[k][0]][arr[k][1]], adj[arr[k][1]][arr[k][0]] = 1, 1
    ans = 0
    for ni in range(1, N + 1):
        visited = [0] * (N + 1)
        visited[ni] = 1
        dfs(ni, 1)

    print('#{} {}'.format(tc, ans))