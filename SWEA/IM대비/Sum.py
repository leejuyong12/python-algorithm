import sys
sys.stdin = open('Sum.txt')

TC = 10
for tc in range(1, TC+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 행
    row_max = 0
    for i in range(100):
        row_sum = 0
        for j in range(len(arr[i])):
            row_sum += arr[i][j]
        if row_sum > row_max:
            row_max = row_sum
    # 열
    col_max = 0
    for j in range(100):
        col_sum = 0
        for i in range(len(arr[j])):
            col_sum += arr[i][j]
        if col_sum > col_max:
            col_max = col_sum
    # 정대각선
    dia_sum = 0
    for i in range(100):
        dia_sum += arr[i][i]
    # 반대각선
    rev_dia_sum = 0
    for i in range(100):
        rev_dia_sum += arr[i][100-i-1]

    print('#{} {}'.format(t, max(row_max, col_max, dia_sum, rev_dia_sum)))