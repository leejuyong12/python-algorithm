import sys
sys.stdin = open('블랙잭.txt')

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))

lst_sum = []    # 3개씩 더한 값을 다 넣어줌
for x in range(N-3+1):
    num = 0
    for y in range(3):
        num += lst[x+y]
    if num <= M:
        lst_sum.append(num)

max_sum = 0
for lst in range(len(lst_sum)):
    if lst_sum[lst] > max_sum:
        max_sum = lst_sum[lst]
print(max_sum)
