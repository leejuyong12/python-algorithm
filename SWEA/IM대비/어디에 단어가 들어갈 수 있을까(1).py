import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt')

# 흰색부분은 1, 검은색 부분은 0

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    final_res = 0
    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[x][y] == 1:
                cnt += 1
            else:
                if cnt == K:
                    final_res += 1
                cnt = 0

        if cnt == K:
            final_res += 1

    for x in range(N):
        cnt = 0
        for y in range(N):
            if arr[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    final_res += 1
                cnt = 0

        if cnt == K:
            final_res += 1

    print(final_res)


