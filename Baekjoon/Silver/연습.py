N = 6
bridge = [[1,2],[2,3],[2,6],[4,5]]

def dfs(V):
    global cnt
    visited[V] = True
    for i in base[V]:
        if not visited[i]:
            dfs(i)
            cnt += 1

base= [[] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0
for i in range(len(bridge)):
    base[bridge[i][0]].append(bridge[i][1])
    base[bridge[i][1]].append(bridge[i][0])
print(base)
dfs(1)
print(cnt-1)