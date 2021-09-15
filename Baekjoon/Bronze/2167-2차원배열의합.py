import sys
sys.stdin = open('input.txt')

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for k in range(K):
    i, j, x, y = list(map(int, input().split()))
    lst_sum = 0
    for r in range(i-1, x):
        for c in range(j-1, y):
            lst_sum += arr[r][c]
    print(lst_sum)

