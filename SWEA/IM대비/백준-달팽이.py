import sys
sys.stdin = open('백준-달팽이.txt')

# 7
# 35
N = int(input())
search = int(input())
arr = [[0]*N for _ in range(N)]

K = N
num = N*N
row = -1
col = 0
row_dir = 1
col_dir = 1
while True:
    for x in range(K):        # 수직이동
        # if row == 0 and col == 0:
        #    return
        row += row_dir
        arr[row][col] = num
        num -= 1

    if K == 0:
        break
    K -= 1

    for y in range(K):        # 수평이동
        col += col_dir
        arr[row][col] = num
        num -= 1
    # 위로 1칸, 오른쪽1칸, 아래로2칸, 왼쪽 2칸, 위로 3칸
    row_dir *= -1
    col_dir *= -1

for x in range(N):
    for y in range(N):
        print(arr[x][y], end=' ')
    print()
for i in range(N):
    for j in range(N):
        if arr[i][j] == search:
            print(i+1, j+1)

# d = 2
# # 위
# for i in range(1, d)
# K == 0:
#
#
# # 오른쪽
# for j in range(1, d)
# d += 1
# # 아래
# for i in range(1, d)
# # 왼쪽
# for i in range(1, d)
