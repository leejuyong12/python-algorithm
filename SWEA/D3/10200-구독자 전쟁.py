TC = int(input())

for tc in range(1, TC+1):
    N, A, B = map(int, input().split())

    # P(A)와 T(B) 채널을 모두 구독하고 있는 사람 최소 최대

    if (A+B) < N:
        minV = 0
        if A < B:
            maxV = A
        elif A > B:
            maxV = B
        else:
            maxV = A

    if (A+B) > N:
        minV = (A+B) - N
        if A > B:
            maxV = B
        elif A < B:
            maxV = A
        else:
            maxV = A

    if (A+B) == N:
        if A > B:
            maxV = B
            minV = 0
        elif A < B:
            maxV = A
            minV = 0
        else:
            maxV = A
            minV = 0
    print('#{} {} {}'.format(tc, maxV, minV))

    # 다른사람 풀이
    # maxV = min(A, B)
    # if A + B > N:
    #    minV = (A + B) - N
    # else:
    #    minV = 0