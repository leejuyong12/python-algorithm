def makeT(node):
    if N-M < node <= N:      # 리프노드면 그대로 안의 번호를 리턴  # 교수님은 tree[node]: 라고 하심
        return tree[node]
    elif node > N:          # 노드 번호에도 안들어오면 그냥 0을 리턴
        return 0
    else:                   # 그 외에는 자식노드를 갖고 있으므로 왼쪽과 오른쪽을 더해주는 과정
        right = makeT(node*2+1)
        left = makeT(node*2)
        tree[node] = left + right
        return tree[node]

TC = int(input())
for tc in range(1, TC+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for i in range(M):
        p, c = map(int, input().split())
        tree[p] = c
    makeT(1)
    print('#{} {}'.format(tc, tree[L]))