import sys
sys.stdin = open('직사각형.txt')

base = [[0] * 100 for _ in range(100)]

for x in range(4):
    lx, ly, rx, ry = map(int, input().split())


    for i in range(lx, rx):
        for j in range(ly, ry):
            base[i][j] = 1

result = 0
for r in range(100):
    for c in range(100):
        result += base[r][c]
print(result)
