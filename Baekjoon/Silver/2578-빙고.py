import sys
sys.stdin = open('2578-백준-빙고.txt')
N = 5
bingo = [list(map(int, input().split())) for _ in range(N)]

num = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(len(num[i])):
        if num[i][j] in bingo[i][j]:
            bingo[i][j] = 0

print(bingo)
