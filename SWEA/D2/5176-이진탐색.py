TC = int(input())

def in_order(n):
    global cnt
    if n <= N:
        in_order(n*2)
        tree[n] = cnt
        cnt += 1
        in_order(n*2+1)

for tc in range(1, TC+1):
    N = int(input())

    tree = [0 for _ in range(N+1)]
    cnt = 1
    in_order(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))

# 교수님 풀이
# def inorder(root):
#     global value
#     if root <= N:
#         inorder(root*2) # root의 왼쪽 서브트리의 root
#         tree[root] = value
#         value += 1
#
#         inorder(root*2+1) # root의 오른쪽 서브트리의 root
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     tree = [0] * (N+1)
#
#     value = 1
#     inorder(1)
#     print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
