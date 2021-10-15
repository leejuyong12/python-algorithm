import sys
sys.stdin = open('[반복문3] 문자삼각형1.txt')

def fill(arr):
    num = ord('A')
    for i in range(N):
        j = i
        k = N - 1
        while j < N:        # i j k 관계 그려보기
            arr[j][k] = chr(num)
            num += 1
            if chr(num) > 'Z':
                num = ord('A')
            k -= 1
            j += 1

def printall(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [[''] * N for _ in range(N)]


    fill(arr)
    print('#{}'.format(tc))
    printall(arr)