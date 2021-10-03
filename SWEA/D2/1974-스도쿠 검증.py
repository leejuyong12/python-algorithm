import sys
sys.stdin = open('스도쿠 검증.txt')

TC = int(input())

for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 행 순회
    for x in range(9):
        for y in range(9):
            arr[x][y]