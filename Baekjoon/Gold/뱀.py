import sys
sys.stdin = open('뱀.txt')

N = int(input())
K = int(input())
base = [[0]* N for _ in range(N)]
snake = 1
# 오른쪽으로 출발
direction = 1
for _ in range(K):
    r, c = map(int, input().split())
    base[r][c] += 1
L = int(input())
for _ in range(L):
    X, C = input().split()
while True:
    