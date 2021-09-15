import sys
sys.stdin = open('2564-경비원-백준.txt')

w, h = map(int, input().split())        # 총 크기  10 5
N = int(input())                        # 3
loc = [list(map(int, input().split())) for _ in range(N)]   # 1-북, 2- 남 / 왼쪽부터의 거리 / 3-서, 4-동 / 위쪽부터의 거리    # 1 4 / 3 2 / 2 8
x, y = map(int, input().split())        # 동근이의 위치   2 3


arr = [[0]*100 for _ in range(100)]

# 동근이의 위치 기록
if x == 1:
    arr[w][y] += 1
elif x == 2:
    arr[0][y] += 1
elif x == 3:
    arr[h-y][0] += 1
elif x == 4:
    arr[h-y][w] += 1
for i in loc:
    if i[0] == 1:
        arr[w][y] += loc.index(i)+1
    elif x == 2:
        arr[0][y] += loc.index(i)+1
    elif x == 3:
        arr[h-y][0] += loc.index(i)+1
    elif x == 4:
        arr[h - y][w] += loc.index(i)+1
print(arr)
