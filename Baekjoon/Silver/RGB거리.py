import sys
sys.stdin = open('RGB거리.txt')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = []
for x in range(1, N):
    # 첫번째부터 각 줄마다 RED, GREEN, BLUE 일 경우로부터 생각해서
    # ex) RED 일때는 전의 GREEN과 BLUE 중 최솟값을 더해가는 식으로 구한다.
    # RED
    lst[x][0] = lst[x][0] + min(lst[x-1][1], lst[x-1][2])
    # GREEN
    lst[x][1] = lst[x][1] + min(lst[x-1][0], lst[x-1][2])
    # BLUE
    lst[x][2] = lst[x][2] + min(lst[x-1][1], lst[x-1][0])

print(min(lst[N-1]))