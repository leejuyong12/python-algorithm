# TC = int(input())
#
# def check(N):
#     global cnt
#     cnt += 1
#     for y in node[N]:
#         check(y)
# for tc in range(1, TC+1):
#     E, N = map(int, input().split())
#     tree = list(map(int, input().split()))
#     # print(tree)
#     node = [[] for _ in range(E+2)]
#     # print(node)
#     idx = 1
#     for x in tree[::2]:
#         node[x].append(tree[idx])
#         idx += 2
#     cnt = 0
#     check(N)
#     # print(node)
#     print('#{} {}'.format(tc, cnt))

# 교수님 풀이

# def preorder(root):
#     global cnt
#     if root:# root 가 가용한 노드인가?
#         cnt += 1
#         preorder(tree[root][0]) # root의 왼쪽 서브트리의 root)
#         preorder(tree[root][1]) # root 의 오른쪽 서브트리의 root)
#
# TC = int(input())
# for tc in range(1, TC+1):
#     E, N = map(int, input().split())
#     s = list(map(int, input().split()))
#     tree = [[0,0] for _ in range(E+2)]
#
#     for i in range(0, len(s), 2):
#         p, c = s[i], s[i+1]
#         if tree[p][0] == 0:     # 처음 나온거면 0이다
#             tree[p][0] = c
#         else:
#             tree[p][1] = c
#     cnt = 0
#     preorder(N)
#     print('#{} {}'.format(tc, cnt))
