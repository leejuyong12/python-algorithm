import sys
sys.stdin = open('로프.txt')

N = int(input())
lst = []
for x in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
for y in range(N):
    lst[y] = lst[y] * (y+1)

print(max(lst))