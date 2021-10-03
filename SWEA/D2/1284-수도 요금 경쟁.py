TC = int(input())

for tc in range(1, TC+1):
    P, Q, R, S, W = map(int, input().split())

    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + (W-R) * S

    if A < B:
        print('#{} {}'.format(tc, A))
    elif A > B:
        print('#{} {}'.format(tc, B))