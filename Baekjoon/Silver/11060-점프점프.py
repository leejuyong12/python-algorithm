import sys
sys.stdin = open('점프점프.txt')

N = int(input())
lst = list(map(int, input().split()))
# 1 2 0 1 3 2 1 5 4 2
dp = [N] * (N)
dp[0] = 0       # 현재 위치에 올 수 있는 최소횟수
# 0 / 1-(1) / 2-min( (2, 3), 2) / 0 / 1-(3) / 3-min( (4,5,6), 4)
# 0     1           2             2     3          4
# dp = [0, 1, 2, 2, 3, 4, 4, 4, 5, 5]
for x in range(len(lst)):
    for y in range(1, lst[x]+1):
        if x + y < N:
            dp[x+y] = min(dp[x+y], dp[x]+1) # dp[x+y]의 값이 있으면 이미 한번 도착했던 기록이 있는것, dp[x]+1 은 1번 움직였을때 1회 추가한 것
        else:           # N보다 크면 이미 목표위치에 도달한거니까 break 걸기
            break
if dp[N-1] != N:        # 처음에 N으로 dp 생성했으므로 N-1번째에 N이 아니면 도착할 수 있다는 뜻이니까 dp[N-1]회 가 최소횟수
    print(dp[N-1])
else:
    print(-1)           # N 그대로이면 올수 없다는 뜻이니까 -1 출력