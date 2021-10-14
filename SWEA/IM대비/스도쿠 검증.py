import sys
sys.stdin = open('스도쿠 검증.txt')

def check(arr):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            row_num = arr[i][j]
            col_num = arr[j][i]

            if row[row_num] > 0:
                return 0
            else:
                row[row_num] += 1
            if col[col_num] > 0:
                return 0
            else:
                col[col_num] += 1

            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        square_num = arr[r][c]
                        if square[square_num] > 0:
                            return 0
                        else:
                            square[square_num] += 1
    return 1


TC = int(input())
for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if check(arr) == 1:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

