import sys
sys.stdin = open('ATM.txt')

N = int(input())
lst = list(map(int, input().split()))

lst.sort()
sum_num = 0
res = 0
for x in range(len(lst)):
    sum_num += lst[x]
    res += sum_num
print(res)