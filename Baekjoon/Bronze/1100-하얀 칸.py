import sys
sys.stdin = open('하얀 칸.txt')

# 0,0 은 하얀 칸
arr = [list(input()) for _ in range(8)]
cnt = 0
for x in range(8):
    for y in range(8):
        if x % 2 == 0 and y % 2 == 0:
            if arr[x][y] == 'F':
                cnt += 1
        if x % 2 == 1 and y % 2 == 1:
            if arr[x][y] == 'F':
                cnt += 1
print(cnt)