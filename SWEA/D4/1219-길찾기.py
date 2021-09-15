def dfs(start, end):
    ST = []
    visited = [False] * (100)
    ST.append(start)
    visited[start] = True
    while ST:
        v = ST.pop(-1)
        if v == end:
            return 1
        for w in GR[v]:
            if visited[w] == False:
                ST.append(w)
                visited[w] = True
    return 0


for tc in range(1, 11):
    num, V = map(int, input().split())

    GR = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    for x in range(0, len(arr), 2):
        GR[arr[x]].append(arr[x + 1])

    print('#{} {}'.format(num, dfs(0, 99)))