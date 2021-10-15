import sys
sys.stdin = open('스도쿠 검증.txt')

def check(arr):
    for i in range(9):
        row_counting = [0] * 10
        for j in range(9):
            row_num = arr[i][j]

            if row_counting[row_num] > 0:
                return 0
            else:
                row_counting[row_num] += 1

    for i in range(9):
        col_counting = [0] * 10
        for j in range(9):
            col_num = arr[j][i]

            if col_counting[col_num] > 0:
                return 0
            else:
                col_counting[col_num] += 1

    for i in range(9):
        for j in range(9):

            if i % 3 == 0 and j % 3 == 0:
                square_counting = [0] * 10

                for x in range(i, i+3):
                    for y in range(j, j+3):
                        square_num = arr[x][y]

                        if square_counting[square_num] > 0:
                            return 0
                        else:
                            square_counting[square_num] += 1
    return 1


TC = int(input())
for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, check(arr)))