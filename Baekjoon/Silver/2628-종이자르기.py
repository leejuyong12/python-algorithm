import sys
sys.stdin = open('2628-종이자르기-백준.txt')

x, y = map(int, input().split())
TC = int(input())
for tc in range(1, TC+1):
    d, num = map(int, input().split())

    arr = [[1]* (x+1) for _ in range(y+1)]
    # 행 순회
    if d == 0:
        for i in range(x+2):
            for j in range(y+2):
                    arr[num][j] = 0
    # 열 순회
    if d == 1:
        for j in range(y+2):
            for i in range(x+2):
                arr[i][num] = 0

    print(arr)



