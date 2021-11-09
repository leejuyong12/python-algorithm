import sys
sys.stdin = open('바이러스.txt')

def dfs(s):
    global cnt
    visited[s] = 1
    for i in arr[s]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

N = int(input())
M = int(input())
arr = [[] * N for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
for x in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


dfs(1)
print(cnt)