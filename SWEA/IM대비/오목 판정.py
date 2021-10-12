import sys
sys.stdin = open('오목 판정.txt')


# def check(arr):
#     # 행우선
#     for x in range(N):
#         cnt_row = 0
#         for y in range(len(arr[x])):
#             if arr[x][y] == 'o':
#                 cnt_row += 1
#             else:
#                 cnt_row = 0
#         if cnt_row == N:
#             return 'YES'
#
#     # 열우선
#     for x in range(N):
#         cnt_col = 0
#         for y in range(len(arr[x])):
#             if arr[y][x] == 'o':
#                 cnt_col += 1
#             else:
#                 cnt_col = 0
#         if cnt_col == N:
#             return 'YES'
#
#
#     # 정대각선우선
#     cnt_dia = 0
#     for x in range(N):
#         if arr[x][x] == 'o':
#             cnt_dia += 1
#         else:
#             cnt_dia = 0
#         if cnt_dia == N:
#             return 'YES'
#
#     # 반대각선우선
#     cnt_rev_dia = 0
#     for x in range(N):
#         for y in range(N):
#             if arr[x][N - x - 1] == 'o':
#                 cnt_rev_dia += 1
#             else:
#                 cnt_rev_dia = 0
#         if cnt_rev_dia == N:
#             return 'YES'

    # return 'NO'
# 8방향 (상, 하, 좌, 우, 좌상대, 좌하대, 우상대, 우하대)
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

def check(r, c):
    for i in range(8):
        cnt = 1
        nr = r + dr[i]
        nc = c + dc[i]
        while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
            cnt += 1
            nr = nr + dr[i]
            nc = nc + dc[i]
        if cnt == 5:
            return True
    return False

def omok():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if check(i, j):
                    return True
    return False
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    if omok():
        ans = 'YES'
    else:
        ans = 'NO'

    print('#{} {}'.format(tc, ans))