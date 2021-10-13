import sys
sys.stdin = open('토글.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr =[[2] + list(map(int, input().split())) + [2] for _ in range(N)]
    arr.insert(0, [2] * (N + 2))
    arr.append([2] * (N + 2))
    k = 1
    cnt = 0
    for k in range(1, M+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if M % k == 0:
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    elif arr[i][j] == 0:
                        arr[i][j] = 1

                else:
                    if (i + j) % k == 0:

                        if arr[i][j] == 1:
                            arr[i][j] = 0
                        elif arr[i][j] == 0:
                            arr[i][j] = 1

    for x in range(1, N+1):
        for y in range(1, N+1):
            if arr[x][y] == 1:
                cnt += 1


    print(cnt)

# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#
#     for k in range(1, M+1): # k의 영역은 1부터 M까지
#         for i in range(N):
#             for j in range(N):
#                 if M % k == 0: # 전체토글
#                     if arr[i][j] == 1:
#                         arr[i][j] = 0
#                     else:
#                         arr[i][j] = 1
#                 elif (i + j +2) % k == 0:
#                     if arr[i][j] == 1:
#                         arr[i][j] = 0
#                     else:
#                         arr[i][j] = 1
#     if k == M:
#         for x in range(N):
#             for y in range(N):
#                 if arr[x][y] == 1:
#                     cnt += 1
#
#     print(f'#{tc} {cnt}')
