import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt')

# 흰색부분은 1, 검은색 부분은 0

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    #행 탐색

    for x in range(N):
        cnt_row = 0

        for y in range(len(arr[x])):
            if arr[x][y] == 1:
                cnt_row += 1
            else:
                if cnt_row == K:
                    result += 1
                cnt_row = 0
        if cnt_row == K:
            result += 1

    # 열 탐색

    for y in range(N):
        cnt_col = 0

        for x in range(len(arr[y])):
            if arr[x][y] == 1:
                cnt_col += 1
            else:
                if cnt_col == K:
                    result += 1
                cnt_col = 0
        if cnt_col == K:
            result += 1
    print('#{} {}'.format(tc, result))

