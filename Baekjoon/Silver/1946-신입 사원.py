import sys
sys.stdin = open('신입사원.txt')

T = int(sys.stdin.readline())
for t in range(T):
    N = int(input())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cnt = 1
    lst.sort(key=lambda x:x[0]) # 서류 기준 정렬
    base = lst[0][1]
    for x in range(1, len(lst)):
        if lst[x][1] < base:
            cnt += 1
            base = lst[x][1]

    print(cnt)