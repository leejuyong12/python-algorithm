import sys
sys.stdin = open('5189-전자카트.txt')
# 순열 사용
def check(k):
    global minV
    if k == N:
        res[-1] = 0
        sumV = 0
        for i in range(N):  # 오른쪽으로
            st = res[i]
            ed = res[i+1]
            sumV += arr[st][ed]
        if minV > sumV:
            minV = sumV
        return

    for i in range(N):  # 아랫쪽으로
        if not visited[i]:
            res[k] = i
            visited[i] = True
            check(k+1)
            visited[i] = False

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = [-1] * (N+1)
    res[0] = 0
    visited = [False] * N
    res[0] = 0
    visited[0] = True
    minV = N * 100
    check(1)

    print('#{} {}'.format(tc, minV))