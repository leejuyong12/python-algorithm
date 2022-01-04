import sys
sys.stdin = open('한줄로서기.txt')

N = int(input())
lst = list(map(int, input().split()))

# base = [0] * N
base = []



# for i in range(N):
#     zero = 0
#     for j in range(N):
#         if zero == lst[i] and base[j] == 0:
#             base[j] = i + 1
#             break
#         elif base[j] == 0:
#             zero += 1

for i in range(N):
    base.insert(lst[N-1-i], N-i)

for x in base:
    print(x, end=' ')