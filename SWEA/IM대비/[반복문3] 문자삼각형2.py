import sys
sys.stdin = open('[반복문3] 문자삼각형2.txt')

def fill():
    num = ord('A')
    s = e = mid
    for i in range(mid, -1, -1):
        for j in range(s, e+1):
            arr[j][i] = chr(num)
            num += 1
            if num > 90:
                num = 65
        s -= 1
        e += 1


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    mid = N // 2
    arr = [[''] * N for _ in range(N)]
    fill()
    print('#{}'.format(tc))
    for x in range(N):
        for y in range(N):
            print(arr[x][y], end = ' ')
        print()