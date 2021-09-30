# 내 풀이
# # 16진수 -> 10진수
#
# def HexToDec(num):
#     if num.isdigit():
#         numV = int(num)
#     else:
#         numV = ord(num) - ord('A') + 10
#     return numV
#
#
# # 10진수 -> 2진수
# def DecToBin(num):
#     res = ''
#     for i in range(3, -1, -1):
#         if num & (1 << i):
#             res += '1'
#         else:
#             res += '0'
#     return res
#
# TC = int(input())
#
# for tc in range(1, TC+1):
#     N, N_16 = map(str, input().split())
#
#     result = ''
#     for x in N_16:
#         result += DecToBin(HexToDec(x))
#
#     print('#{} {}'.format(tc, result))


# # 교수님 풀이
# def hexToBin(hexV):
#     # 1. 16진수를 10진수로 바꾼다
#     if hexV.isdigit():
#         numV = int(hexV)
#     else:
#         numV = ord(hexV) - ord('A') + 10
#
#     # 2. 10진수를 2진수 문자열
#     res = ''
#     for j in range(3, -1, -1):
#         if numV & 1 << j:
#             res += '1'
#         else:
#             res += '0'
#     return res
#
#
# TC = int(input())
#
# for tc in range(1, TC+1):
#     N, M = map(str, input().split())
#
#     res = ''
#     for i in range(int(N)):
#         res += hexToBin(M[i])
#
#     print(res)

# dictionary 활용 방법도 있음!
# def hexToBin(hexV):
# dict = {'0' : '0000', '1':'0001' ....}
    # return dict[hexV]