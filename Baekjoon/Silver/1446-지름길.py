import sys
sys.stdin = open('지름길.txt')

N, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

