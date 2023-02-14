import sys
sys.stdin = open('9251-LCS.txt')

A = list(input())
B = list(input())
dp = [0] * max( len(A), len(B) )

cnt = 0
#       A  C  A  Y  K  P
#   C   0  1  0  0  0  0
#   A   1  1  2  0  0  0
#   P   1  1  2  0  0  3
#   C   1  2  2  0  0  3
#   A   1  2  3  0  0  3
#   K   1  2  3  0  4  3
for x in range(len(A)):
     cnt_1 = 0
     for y in range(len(B)):
         if cnt_1 < dp[y]:
             cnt_1 = dp[y]
         elif A[x] == B[y]:
             dp[y] = cnt_1 + 1
print(max(dp))

