import sys
sys.stdin = open('제곱수의합.txt')

N = int(input())
dp = [0] * (N+1)


# import math
# N = int(input())
# cnt = 0
# while N > 0:
#     start = math.trunc(N**(1/2))
#     N -= start**2
#     if N < start**2:
#         if start > 1:
#             start -= 1
#
#     cnt += 1
# print(cnt)
