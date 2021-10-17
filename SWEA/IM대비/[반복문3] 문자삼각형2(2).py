import sys
sys.stdin = open('[반복문3] 문자삼각형2.txt')

def fill(arr):
    num = ord('A')
    start = end = mid
    for i in range(mid, -1, -1):
        for j in range(start, end+1):
            arr[j][i] = chr(num)
            num += 1
            if chr(num) > 'Z':
                num = ord('A')
        start -= 1
        end += 1


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    mid = N // 2
    arr = [['']* N for _ in range(N)]
    fill(arr)
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()