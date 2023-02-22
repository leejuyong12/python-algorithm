import sys
sys.stdin = open('11501-주식.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    sum_result = 0
    tmp = 0
    for x in range(len(lst)-1, -1, -1):

        if lst[x] > tmp:
            tmp = lst[x]
        else:
            sum_result += (tmp - lst[x])

    print(sum_result)

