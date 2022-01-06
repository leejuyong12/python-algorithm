import sys
sys.stdin = open('보물.txt')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
# A.sort(reverse=True)
# B.sort()
# for x in range(N):
#     S += A[x] * B[x]
# print(S)
A.sort()
for x in range(N):
    S += A[x] * B.pop(B.index(max(B)))
print(S)