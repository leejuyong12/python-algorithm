TC = int(input())

for tc in range(1, TC+1):
    A, B = map(int, input().split())

    time = 0
    base = (A + B) // 24
    if A + B >= 24:
        time = A+B-(24*base)

    elif A + B < 24:
        time = A + B
    print('#{} {}'.format(tc, time))