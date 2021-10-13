import sys
sys.stdin = open('N-Queen.txt')
    # 상  하 좌  우  좌상  좌하  우상  우하
dr = [-1, 1, 0, 0,  -1,   1,   -1,   1]
dc = [0,  0, -1, 1,  -1,  -1,   1,   1]

def check():

    for x in range(N):
        for y in range(N):



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    visited = [[0] * N for _ in range(N)]


