import sys
sys.stdin = open('톱니바퀴.txt')

def rotate_right(num, dir):
    if arr[num-1][]
def rotate_left(num, dir):

# 0은 N극, 1은 S극

arr = [list(map(int, input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    # a는 톱니바퀴 번호, b는 회전방향 # b = 1은 시계, -1은 반시계
    num, dir = map(int, input().split())

    if arr[num-1][2] != arr[]