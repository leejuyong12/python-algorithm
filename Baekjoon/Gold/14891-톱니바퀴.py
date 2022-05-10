import sys
sys.stdin = open('톱니바퀴.txt')

arr = [list(map(int, input().split())) for _ in range(4)]
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    # 모르겠다..