import sys
sys.stdin = open('2605-줄세우기-백준.txt')

N = int(input())

lst = list(map(int, input().split()))

result = []

for i in range(N):
    result.insert(i-lst[i],i+1)

for x in result:
    print(x, end = ' ')