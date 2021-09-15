import sys
sys.stdin = open('2635-백준.txt')


N = int(input())



for x in range(N+1):
    lst = [N, x]

    y = 0
    while True:
        min_num = lst[y] - lst[y+1]


