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
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
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

import sys
sys.stdin = open('그룹 나누기.txt')

#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

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


