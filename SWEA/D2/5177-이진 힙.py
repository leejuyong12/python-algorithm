def heap(node):
    parents_node = node // 2
    if parents_node >= 0:
        if tree[parents_node] > tree[node]:
            tree[parents_node], tree[node] = tree[node], tree[parents_node]
            heap(parents_node)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    num = 1
    tree = [0] + list(map(int, input().split()))
    for x in range(len(tree)-1):
        heap(num)
        num += 1
    sum_num = 0
    while N:
        N //= 2
        sum_num += tree[N]
    print('#{} {}'.format(tc, sum_num))

# 교수님 풀이
#
# def makeT(idx):
#     if idx == 1:    # idx에 있는 데이터의 우선순위 > 부모노드에 있는 데이터의 우선순위
#         return
#     if tree[idx] < tree[idx//2]:
#         tree[idx], tree[idx // 2] = tree[idx // 2], tree[idx]
#         makeT(idx // 2)
# def getSum():
#     sumV = 0
#     idx = N // 2
#     while idx >= 1:
#         sumV += tree[idx]
#         idx //= 2
#     return sumV
#
# # 바로 위의 getSum 재귀 방식
# # def getSum2(idx):
# #     global sumV2
# #     if idx:
# #         sumV2 += tree[idx]
# #         getSum2(idx//2)
# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     lst = [0] + list(map(int, input().split()))
#     tree = [0] * (N+1)
#     for i in range(1, N+1):
#         tree[i] = lst[i]
#         makeT(i)
#     getSum()