import sys
sys.stdin = open('2+1세일.txt')

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort(reverse=True)
cost = 0
for i in range(N):
    if i % 3 != 2:
        cost += lst[i]
print(cost)

# N = int(sys.stdin.readline())
# lst = [int(sys.stdin.readline()) for _ in range(N)]
# lst.sort(reverse=True)
# cost = sum(lst)
# for i in range(2, N,3):
#     cost -= lst[i]
# print(cost)