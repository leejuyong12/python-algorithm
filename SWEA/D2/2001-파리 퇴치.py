TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            lst_sum = 0
            for r in range(i, i + M):
                for c in range(j, j + M):
                    lst_sum += arr[r][c]
            if lst_sum > max_sum:
                max_sum = lst_sum
    print('#{} {}'.format(tc, max_sum))