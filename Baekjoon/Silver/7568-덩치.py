import sys
sys.stdin = open('덩치.txt')

N = int(input())
check = [list(map(int, input().split())) for _ in range(N)]
for x in check:
    rnk = 1
    for y in check:
        if x[0] < y[0] and x[1] < y[1]: # 단순 이중 for반복문
            rnk += 1
    print(rnk, end= ' ')