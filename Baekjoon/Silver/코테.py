import sys
sys.stdin = open('코테.txt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

tmp_M = M
max_chk = max(lst)
min_chk = 0
cnt = 0

for x in lst:
    if x > M:
        max_chk = min(max_chk, x)
    elif x == M:
        print(x)
        break
    elif min_chk < M and cnt < 3:
        min_chk += x
        cnt += 1
if max_chk > M and min_chk > M:
    print(min(max_chk, min_chk))
elif max_chk > M and min_chk < M:
    print(max_chk)
elif max_chk < M and min_chk < M:
    print('IMPOSSIBLE')
elif max_chk < M and min_chk > M:
    print(min_chk)