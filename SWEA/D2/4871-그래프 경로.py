def dfs(s):

    ST = []
    visited = [False] * (V+1)

    ST.append(s)
    visited[s] = True
    while ST:
        v = ST.pop(-1)
        if v == G:
            return 1

        for w in GR[v]:
            if visited[w] == False:
                ST.append(w)
                visited[w] = True
    return 0
TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())

    GR = [[] for _ in range(V+1)]

    for i in range(E):
        v1, v2 = map(int, input().split())
        GR[v1].append(v2)

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, dfs(S)))
