import sys
sys.stdin = open('IM.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lights = [0] + list(map(int, input().split()))    # 목표 결과, 자릿수 1부터 일치시키기 위해 [0] 추가

    base = [0] * (N+1)                              # 자릿수 맞추기 위해 N+1
    cnt = 0
    for x in range(1, N+1):
        if lights[x] != base[x]:                       # 같지 않으면
            for y in range(x, N+1, x):                 # x만큼 뛰어넘기 - 배수를 의미
                if base[y] == 0:
                    base[y] = 1
                else:
                    base[y] = 0
            cnt += 1                                  # 한 숫자의 배수가 다 돌면 cnt 1 추가
    print(cnt)