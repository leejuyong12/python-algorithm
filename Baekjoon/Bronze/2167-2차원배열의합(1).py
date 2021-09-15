import sys
sys.stdin = open('2167-백준-2차원배열의합.txt')

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
for k in range(K):
    i, j, x, y = map(int, input().split())

    sum_num = 0
    for r in range(i-1, x):
        for c in range(j-1, y):
            sum_num += arr[r][c]
    print(sum_num)
