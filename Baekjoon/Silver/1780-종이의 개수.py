import sys
sys.stdin = open('종이의 개수.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
