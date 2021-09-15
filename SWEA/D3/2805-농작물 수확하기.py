TC = int(input())
for tc in range(1, TC + 1):
    t = int(input())

    arr = [list(map(int, input())) for _ in range(t)]

    farm = 0

    i = 0
    while i <= t // 2:
        farm += arr[i][t // 2]
        for j in range(1, i + 1):
            farm += arr[i][(t // 2) - j] + arr[i][(t // 2) + j]
        i += 1

    i_2 = t // 2 + 1
    while t // 2 < i_2 < t:
        farm += arr[i_2][t // 2]
        for j in range(1, t - i_2):
            farm += arr[i_2][(t // 2) - j] + arr[i_2][(t // 2) + j]
        i_2 += 1
    print('#{} {}'.format(tc, farm))