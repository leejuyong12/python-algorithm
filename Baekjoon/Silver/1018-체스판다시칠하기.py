import sys
sys.stdin = open('1018-백준-체스판다시칠하기.txt')

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
W = ['W', 'B'] * 4
w = []
B = ['B', 'W'] * 4
b = []
for x in range(1, 9):
    if arr[0][0] == 'W':
        if x % 2 == 1:
            w.append(W)
        else:
            w.append(B)
    if arr[0][0] == 'B':
        if x % 2 == 1:
            w.append(B)
        else:
            w.append(W)

lst = []
# N, M이 각각 8보다 크거나 같다면 자르기
for x in range(N-7):
    for y in range(M-7):
        cnt_w = 0
        cnt_b = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if  (i+j) % 2 == 0:
                    if arr[i][j] != 'W':
                        cnt_w += 1
                    if arr[i][j] != 'B':
                        cnt_b += 1
                else:
                    if arr[i][j] != 'B':
                        cnt_w += 1
                    if arr[i][j] != 'W':
                        cnt_b += 1

        lst.append(cnt_w)
        lst.append(cnt_b)
print(min(lst))




