def exercise(L, U, X):
    if L <= X <= U:
        return 0
    elif X < L:
        return L - X
    elif U < X:
        return -1


TC = int(input())
for tc in range(1, TC + 1):
    L, U, X = map(int, input().split())

    time = exercise(L, U, X)

    print('#{} {}'.format(tc, time))