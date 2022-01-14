import sys
sys.stdin = open('블로그2.txt')

N = int(sys.stdin.readline())
goal = list(sys.stdin.readline().rstrip())
cnt = 1
start = goal[0]
for x in range(N-1):
    if goal[x] != goal[x+1] and start != goal[x+1]:
        cnt += 1
print(cnt)

# N = int(sys.stdin.readline())
# goal = list(sys.stdin.readline().rstrip())
#
# if goal.count('B') > goal.count('R'):
#     base = ['B'] * N
# else:
#     base = ['R'] * N
# cnt = 1
# tmp = 0
# while tmp < N:
#     if goal[tmp] != base[tmp]:
#         cnt += 1
#         for y in range(tmp+1, N):
#             if goal[tmp] == base[tmp]:
#                 tmp += y-1
#                 break
#     tmp += 1
#
# print(cnt)

