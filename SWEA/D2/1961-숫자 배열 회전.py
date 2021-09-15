def change(arr, N):  # 파라미터 2개 주기
    arr_clear = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr_clear[i][j] = arr[N - j - 1][i]

    return arr_clear


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]  # int 가 아니라 str인거 주의

    change_90 = change(arr, N)
    change_180 = change(change_90, N)
    change_270 = change(change_180, N)

    print('#{}'.format(tc))
    for x in range(N):
        print(''.join(change_90[x]), ''.join(change_180[x]), ''.join(change_270[x]))  # join 활용법!
