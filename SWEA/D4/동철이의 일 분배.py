import sys
sys.stdin = open('동철이.txt')

def check(x, mul):
    global result

    if x == N:
        if result < mul:
            result = mul
            return
    if result >= mul:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            check(x+1, mul * arr[x][i]/100)
            visited[i] = 0

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    visited = [0] * N
    result = 0
    check(0, 1)
    print(f'#{tc} {result*100:6f}')
