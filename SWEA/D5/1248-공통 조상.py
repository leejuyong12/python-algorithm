import sys
sys.stdin = open('공통 조상.txt')

TC = int(input())
for tc in range(1, TC+1):
    V, E, n1, n2 = map(int, input().split())
    tree = list(map(int, input().split()))
    parent = [0] * (V+1)
    for x in range(0, len(tree), 2):
        parent[tree[x]] = tree[x]
    n1_lst = [n1]
    n2_lst = [n2]
    while parent[n1]:
        n1_lst.append(parent[n1])
        n1 = parent[n1]
    while parent[n2]:
        n2_lst.append(parent[n2])
        n2 = parent[n2]

    n1_last = len(n1_lst)-1
    n2_last = len(n2_lst)-1

    while n1_lst[n1_last] == n2_lst[n2_last]:
        n1_last -= 1
        n2_last -= 1
    print(n2_last)
