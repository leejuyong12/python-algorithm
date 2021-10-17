import sys
sys.stdin = open('줄 세우기.txt')

N = int(input())
lst = list(map(int, input().split()))

new = []

for x in range(N):
    new.insert(x-lst[x], x+1)
print(new)