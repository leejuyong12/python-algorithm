import sys
sys.stdin = open('Magnetic.txt')

TC = 10
for tc in range(1, TC+1):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for x in range(100):
        is_N = 0
        for y in range(100):
            if is_N == 0 and arr[y][x] == 1:
                is_N = 1
            elif is_N == 1 and arr[y][x] == 2:
                cnt += 1
                is_N = 0
    print('#{} {}'.format(tc, cnt))