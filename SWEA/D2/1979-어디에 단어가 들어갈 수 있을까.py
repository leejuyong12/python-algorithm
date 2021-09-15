TC = int(input())

for tc in range(1, TC + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(N):
        cnt_i = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt_i += 1
            else:
                if cnt_i == K:
                    total += 1
                cnt_i = 0
        if cnt_i == K:
            total += 1

    for i in range(N):
        cnt_j = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt_j += 1
            else:
                if cnt_j == K:
                    total += 1
                cnt_j = 0
        if cnt_j == K:
            total += 1

    print('#{} {}'.format(tc, total))