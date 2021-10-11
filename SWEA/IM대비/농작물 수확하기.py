import sys
sys.stdin = open('농작물 수확하기.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    value_sum = 0
    i = 0
    while i <= N//2:                                # 중앙 행까지
        value_sum += arr[i][N//2]
        for j in range(1, i+1):
            value_sum += arr[i][(N//2)-j] + arr[i][(N//2)+j]
        i += 1

    i_1 = N//2 + 1                                  # 중앙 행 밑으로
    while N//2 < i_1 < N:
        value_sum += arr[i_1][N//2]
        for j in range(1, N-i_1):
            value_sum += arr[i_1][N//2-j] + arr[i_1][N//2+j]
        i_1 += 1
    print('#{} {}'.format(tc, value_sum))
