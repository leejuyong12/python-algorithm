import sys
sys.stdin = open('2669-백준.txt')

lst = [[0]*100 for _ in range(100)]
for nums in range(4):
    x, y, r, c = map(int, input().split())

    for i in range(x, r):
        for j in range(y, c):
            lst[i][j] = 1

result = 0
for a in range(len(lst)):
    for b in range(len(lst)):
        if lst[a][b] > 0:
            result += 1
print(result)