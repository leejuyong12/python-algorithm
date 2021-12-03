import sys
sys.stdin = open('동철이.txt')

def check(x, work):
    global result
    if x == N:
        if result < work:
            result = work
            return

    if result >= work:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            check(x+1, work * arr[x][i]/100)
            visited[i] = 0

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N
    check(0,1)
    print(f'#{tc} {result*100:6f}')