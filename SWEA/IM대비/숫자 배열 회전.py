import sys
sys.stdin = open('숫자 배열 회전.txt')

def change(arr, N):
    new_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-j-1][i]

    return new_arr
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    new_arr = [[0]*N for _ in range(N)]

    change_90 = change(arr, N)
    change_180 = change(change_90, N)
    change_270 = change(change_180, N)

    print('#{}'.format(tc))
    for x in range(N):
        print(''.join(change_90[x]), ''.join(change_180[x]), ''.join(change_270[x]))
