import sys
sys.stdin = open('최소 신장 트리.txt')

def prim():
    # curV = 0
    s = 0
    D[s][0] = 0

    while len(U) <= V:
        # D의 key값이 최소이고 U에 포함되지 않은 정점을 구한다.
        minV = 1000000
        for i in range(V+1):
            if i in U:
                continue
            if D[i][0] < minV: # 위의 코드 지우고 여기에 i not in U and 해도 된다.
                minV = D[i][0]
                curV = i

        # U에 추가
        U.append(curV)

        # curV의 인접한 정점의 가중치를 사용하여 D를 업데이트
        for i in range(V+1):
            if i in U:
                continue
            if G[curV][i] > 0:
                if D[i][0] > G[curV][i]:
                    D[i][0] = G[curV][i]
                    D[i][1] = curV


TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())

    G = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s1, s2, w = map(int, input().split())
        G[s1][s2] = w
        G[s2][s1] = w
    D = [[1000000, 0] for _ in range(V+1)]
    U = []
    prim()
    res = 0
    for x in D:
        res += x[0]
    print('#{} {}'.format(tc, res))
