import sys
sys.stdin = open('블랙잭.txt')

# N, M = list(map(int, input().split()))
# lst = list(map(int, input().split()))
#
# lst_sum = []    # 3개씩 더한 값을 다 넣어줌
# for x in range(N-3+1):
#     num = 0
#     for y in range(3):
#         num += lst[x+y]
#     if num <= M:
#         lst_sum.append(num)
#
# max_sum = 0
# for lst in range(len(lst_sum)):
#     if lst_sum[lst] > max_sum:
#         max_sum = lst_sum[lst]
# print(max_sum)
# 규칙 : N장의 카드를 모두 숫자가 보이도록 바닥에 놓고, 딜러가 숫자 M을 말함
# 플레이어는 제한된 시간 안에서 N장의 카드 중에서 3장을 골라야 한다.
# M 을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = []
for x in range(N-2):
    for y in range(x+1, N-1):
        for z in range(y+1, N):
            if lst[x] + lst[y] + lst[z] <= M:
                result.append(lst[x] + lst[y] + lst[z])
print(max(result))
