import sys
sys.stdin = open('부분 수열의 합.txt')

def


TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0