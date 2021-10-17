import sys
sys.stdin = open('사냥꾼.txt')

# 0은 빈공간, 1은 사냥꾼, 2는 토끼, 3은 바위
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

