import sys
sys.stdin = open('[반복문3] 문자삼각형2.txt')

def fill():
    num = ord('A')
    s = e = mid
    for i in range(mid, -1, -1):
        for j in range(s, e+1):
            arr[j][i] = chr(num)
            num += 1
            if chr(num -1) == 'Z':
                num = ord('A')
        s -= 1
        e += 1

def printall():
    for i in range(N):
        for j in range

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    mid = N // 2
    arr = [ [' '] * (mid + 1) for _ in range(N)]

    fill