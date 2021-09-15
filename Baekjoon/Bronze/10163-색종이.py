import sys
sys.stdin = open('10163-백준-색종이.txt')

TC = 3
for tc in range(TC):
    arr = [[0]*1001 for _ in range(1001)]
    N = int(input())
    colored = [0] * (N+1)

    for n in range(1, N+1):
        x, y, w, h = map(int, input().split())

        for i in range(x, x+w): #
            for j in range(y, y+h):
                arr[i][j] = n
    for z in arr:
        for num in z:
            if num:
                colored[num] += 1

    for t in range(1, N+1):
        print(colored[t])



