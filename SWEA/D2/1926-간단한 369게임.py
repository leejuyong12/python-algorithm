import sys
sys.stdin = open('스도쿠 검증.txt')

def check():
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
                                    # 가로 세로 검사
            num1 = arr[i][j]        # 가로 숫자
            num2 = arr[j][i]        # 세로 숫자
            if row[num1]:   # 스도쿠의 숫자를 각 자리 index로 활용
                return 0    # 이미 숫자가 있는데 또 나오면 0을 출력
            if col[num2]:
                return 0
            row[num1] = col[num2] = 1       # 그 외에는 1을 집어넣어서 이미 숫자가 있다는 것을 1로 표현

            if i % 3 == 0 and j % 3 == 0:   # 내부 사각형 검사
                square = [0] * 10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = arr[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    return 1



TC = int(input())

for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if check() == 1:
        print('#{} 1'.format(tc))
    elif check() == 0:
        print('#{} 0'.format(tc))
