def per(k,sumV):    # sumV 추가
    global minV
    if sumV > minV:     # 시간초과에서 추가
        return
    if k == N:
            # t를 기준으로 2차원배열에서 합을 구한다.
        #sumV = 0
        # for i in range(N):        # 시간초과에서 삭제
        #     sumV += arr[i][t[i]]
        if minV > sumV:
            minV = sumV
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                t[k] = i
                per(k+1, sumV+arr[k][i]) # 시간초과에서 추가
                visited[i] = False
TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    t = [-1] * N
    visited = [False] * N
    minV = 10*N

    per(0,0)

    print('#{} {}'.format(tc, minV))