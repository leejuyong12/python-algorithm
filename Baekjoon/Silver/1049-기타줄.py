import sys
sys.stdin = open('기타줄.txt')

N, M = map(int, input().split())     # 적어도 N 개를 사야 한다.
a_lst = []
b_lst = []
for x in range(M):
    a, b = map(int, input().split())
    a_lst.append(a)
    b_lst.append(b)

min_6 = min(a_lst)
min_1 = min(b_lst)
if min_6 < min_1 * 6:
    if min_6 < (N%6) * min_1:
        print((N//6)* min_6 + min_6)
    else:
        print((N//6)*min_6 + (N%6)*min_1)
else:
    print(min_1 * N)