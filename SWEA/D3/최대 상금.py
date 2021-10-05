import sys
sys.stdin = open('최대 상금.txt')

# def sorts(base):        # base = 123
#     global change
#     n = len(base)       # n = 3
#     for i in range(n-1):        # i = 0, 1
#         maxI = i                # maxI = 0    // maxI = 1
#         for j in range(i+1, n): # i = 0 j = 1, 2  // i = 1 j = 2
#             if base[j] >= base[maxI]:
#                 maxI = j                #
#         base[maxI], base[i] = base[i], base[maxI]
#         change -= 1
#         if change == 0:
#             return base
#
# TC = int(input())
#
# for tc in range(1, TC+1):
#     base, change = input().split()        # str(123), str(1)
#     base = list(base)
#     change = int(change)
#     sorts(base)
#     base = ''.join(base)
#     print('#{} {}'.format(tc, base))

#재귀
def solve(k):   # k 는 바꾸는 횟수
    global maxV
    if k == int_change:
        intV = int(''.join(lst_base))
        if maxV < intV:
            maxV = intV
        return

    L = len(base)
    for i in range(0, L-1):
        for j in range(i+1, L):
            lst_base[i], lst_base[j] = lst_base[j], lst_base[i]
            solve(k+1)
            lst_base[i], lst_base[j] = lst_base[j], lst_base[i]

TC = int(input())

for tc in range(1, TC+1):
    base, change = input().split()        # str(123), str(1)
    lst_base = list(base)
    int_change= int(change)
    maxV = 0
    solve(0)
    print('#{} {}'.format(tc, maxV))