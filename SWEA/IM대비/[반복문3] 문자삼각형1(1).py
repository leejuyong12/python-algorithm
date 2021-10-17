import sys
sys.stdin = open('[반복문3] 문자삼각형1.txt')

def fill(arr):
    num = ord('A')
    for i in range(N):
        k = N-1
        while i < N:
            arr[i][k] = chr(num)
            num += 1
            if chr(num) > 'Z':
                num = ord('A')
            k -= 1
            i += 1

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [['']* N for _ in range(N)]

    fill(arr)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end= ' ')
        print()