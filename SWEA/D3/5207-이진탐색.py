import sys
sys.stdin = open('이진탐색.txt')

def binarySearch(N, A, B):

    global result
    for b in B:
        dir = 0
        l = 0
        r = N - 1
        while l <= r:
            m = (l + r) // 2

            if A[m] == b:
                result += 1
                break

            elif A[m] > b:
                r = m - 1
                if dir == 1:
                    break
                dir = 1
            else:
                l = m + 1
                if dir == -1:
                    break
                dir = -1

    return result


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    result = 0
    print('#{} {}'.format(tc, binarySearch(N, A, B)))


#
# 교수님 풀이
# def chk(lst, key):
#     l = 0
#     r = len(lst) -1
#     di = 0
#     while l <= r:
#         m = (l+r) // 2
#         if key == lst[m]:
#             return 1
#
#         if key < lst[m]:
#             if di == 'L':
#                 return 0
#             r = m-1
#             di = 'L'
#         else:
#             if di == 'R':
#                 return 0
#             l = m+1
#             di = 'R'
#     return 0
# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())
#     A = sorted(list(map(int, input().split())))
#     B = list(map(int, input().split()))
#     result = 0
#     for b in B:
#         chk(A, )
#     print('#{} {}'.format(tc, binarySearch(N, A, B)))