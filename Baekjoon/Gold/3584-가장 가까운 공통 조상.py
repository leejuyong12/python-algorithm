import sys
sys.stdin = open('가장 가까운 공통 조상.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    parent = [0] * (N+1)
    for n in range(N-1):
        p, c = map(int, input().split())
        parent[c] = p
    n1, n2 = map(int, input().split())

    n1_lst = [n1]       # n1의 부모의 부모의 부모의 계속 저장
    n2_lst = [n2]       # n2의 부모의 부모의 부모의 계속 저장장

   # 부모노드가 없을때까지 계속 불러와
    while parent[n1]:
        n1_lst.append(parent[n1])
        n1 = parent[n1]
    while parent[n2]:
        n2_lst.append(parent[n2])
        n2 = parent[n2]

    # 뒤에서부터 탐색해서 다른거 나오면 그 전꺼 출력
    n1_last = len(n1_lst)-1
    n2_last = len(n2_lst)-1

    while n1_lst[n1_last] == n2_lst[n2_last]:
        n1_last -= 1
        n2_last -= 1
    print(n1_lst[n1_last + 1])

