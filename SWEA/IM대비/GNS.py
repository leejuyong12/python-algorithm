import sys
sys.stdin = open('GNS.txt')

TC = int(input())
for tc in range(1, TC+1):
    tn, n = input().split()
    lst = list(input().split())

    base = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    counting_lst = [0] * 10

    for x in lst:
        counting_lst[base.index(x)] += 1

    res = ''
    for y in range(len(counting_lst)):
        res += (base[y] + ' ') * counting_lst[y]
    print('{}'.format(tn))
    print(res)

# 방법 2
# TC = int(input())
# for tc in range(TC):
#     TC_num, N = input().split()
#     lst = list(input().split())
#     N = int(N)
#     lst_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     result = []
#     for j in range(len(lst_num)):
#         for i in range(N):
#             if lst[i]==lst_num[j]:
#                 result.append(lst[i])
#     print(TC_num, end=' ')
#     print(*result)