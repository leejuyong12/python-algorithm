import sys
sys.stdin = open('어디에 단어가.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 행 검색
    for x in range(N):
        check_x = 0
        for y in range(N):
            if arr[x][y] == 1:
                check_x += 1
            else:               # 0이 나오는데 이미 check_x 가 K이면 cnt 올려주고 초기화
                if check_x == K:
                    cnt += 1
                check_x = 0
        if check_x == K:
            cnt += 1

    for x in range(N):
        check_y = 0
        for y in range(N):
            if arr[y][x] == 1:
                check_y += 1
            else:
                if check_y == K:
                    cnt += 1
                check_y = 0
        if check_y == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))