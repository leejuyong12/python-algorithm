import sys
sys.stdin = open('Magnetic.txt')

TC = 10
for tc in range(1, TC+1):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(T)]

    cnt = 0
    for x in range(T):                      # 입력값 N극은 1 S극은 2
        is_N = 0                            # N극이 없으면 0 있으면 1
        for y in range(len(arr[x])):        # 열우선
            if is_N == 0 and arr[y][x] == 1:    # N극 찾기
                is_N = 1
            elif is_N == 1 and arr[y][x] == 2:  # S극 찾기
                cnt += 1
                is_N = 0                        # 짝이 맞았으니 다시 초기화
    print('#{} {}'.format(tc, cnt))