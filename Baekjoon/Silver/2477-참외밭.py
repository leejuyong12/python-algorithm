import sys
sys.stdin = open('2477-참외밭-백준.txt')

K = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]    # 1-동쪽, 2-서쪽, 3-남쪽, 4-북쪽

max_w = 0
max_h = 0
w_idx = 0
h_idx = 0

for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if max_w < arr[i][1]:
            max_w = arr[i][1]
            w_idx = i
    if arr[i][0] == 3 or arr[i][0] == 4:
        if max_h < arr[i][1]:
            max_h = arr[i][1]
            h_idx = i

min_w = 0
if arr[(w_idx-1)%6][1] > arr[(w_idx+1)%6][1]:
    min_w = arr[(w_idx-1)%6][1] - arr[(w_idx+1)%6][1]
elif arr[(w_idx-1)%6][1] < arr[(w_idx+1)%6][1]:
    min_w = arr[(w_idx + 1) % 6][1] - arr[(w_idx - 1) % 6][1]
min_h = 0
if arr[(h_idx-1)%6][1] > arr[(h_idx+1)%6][1]:
    min_h = arr[(h_idx-1)%6][1] - arr[(h_idx+1)%6][1]
elif arr[(h_idx-1)%6][1] < arr[(h_idx+1)%6][1]:
    min_h = arr[(h_idx + 1) % 6][1] - arr[(h_idx - 1) % 6][1]
result = (max_w * max_h) - (min_w * min_h)
print(result * K)