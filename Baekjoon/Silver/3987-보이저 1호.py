import sys
sys.stdin = open('보이저 1호.txt')

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
PR, PC = map(int, input().split())

row = PR
col = PC
U = -1
R = 1
D = 1
L = -1

while True:

