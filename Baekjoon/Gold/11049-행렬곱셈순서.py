import sys
sys.stdin = open('11049-행렬곱셈순서.txt')

N = int(input())
lst = []
dp = [[0] * N]
for x in range(N):
    r, c = map(int, input().split())
    lst.append([r,c])
