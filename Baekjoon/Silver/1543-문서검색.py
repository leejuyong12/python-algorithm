import sys
sys.stdin = open('문서검색.txt')

# def check(target, search):
#     N = len(target)
#     M = len(search)
#     cnt = 0
#     i = 0
#     while i < N-M+1:
#         j = 0
#         while j < M and target[i+j] == search[j]:
#             j += 1
#         if j >= M:
#             cnt += 1
#             i += j
#         else:
#             i += 1
#     return cnt + N - (cnt * M)
#
# target = input()
# search = input()
#
# print(check(target, search))

# 엄청 쉬운데 이걸 못푸네...
target = input()
search = input()
cnt = 0
i = 0
while i <= len(target) - len(search) + 1:
    if target[i:i+len(search)] == search:
        cnt += 1
        i += len(search)
    else:
        i += 1
print(cnt)