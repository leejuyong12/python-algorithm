import sys
sys.stdin = open('12865-평범한 배낭.txt')

N, K = map(int, input().split()) # 갯수, 무게
#arr = [list(map(int, input().split())) for _ in range(N)] # 무게, 가치
arr = [[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = arr[i][0]  # 현재 물건 무게
        val = arr[i][1]     # 현재 물건 가치
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else: # j >= weight
            knapsack[i][j] = max(knapsack[i-1][j], val + knapsack[i-1][j-weight])
            # max(knapsack[이전 물건][현재 가방 무게], 현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게])
print(knapsack[N][K])
# 냅색 알고리즘
# 이차원 배열로 만들기



# 내 코드
# N, K = map(int, input().split()) # 갯수, 무게
# lst = [list(map(int, input().split())) for _ in range(N)] # 무게, 가치
#
# lst.sort(reverse=True, key=lambda x:x[0])
# max_val = 0
# max_weight = 0
# tmp_K = K
# tmp_val = 0
# for x in range(N):
#     if lst[x][0] <= K:
#         tmp_val += lst[x][1]
#         tmp_K -= lst[x][0]
#         for y in range(x+1, N):
#             if tmp_K >= lst[y][0]:
#                 tmp_val += lst[y][1]
#                 tmp_K -= lst[y][0]
#
#             if max_val < tmp_val:
#                 max_val = tmp_val
#             tmp_val = 0
#             tmp_K = K
# print(max_val)

