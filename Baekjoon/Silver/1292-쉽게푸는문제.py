import sys
sys.stdin = open('1292-SWEA-쉽게푸는문제.txt')

A, B = map(int, input().split())

lst = [0]
for x in range(1001):
    lst += [x] * x
sum_num = 0
for y in range(A, B+1):
    sum_num += lst[y]
print(sum_num)