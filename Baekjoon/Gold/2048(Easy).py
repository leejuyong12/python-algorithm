import sys
sys.stdin = open('2048.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)