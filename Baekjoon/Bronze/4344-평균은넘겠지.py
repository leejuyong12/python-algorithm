import sys
sys.stdin = open('4344-백준-평균은넘겠지.txt')

TC = int(input())

for tc in range(1, TC+1):
    info = list(map(int, input().split()))

    N = info[0]

    sum_point = 0
    for x in range(1, N+1):
        sum_point += info[x]

    avg_point = sum_point / N

    over_N = 0
    for y in range(1, N+1):
        if avg_point < info[y]:
            over_N += 1

    print('{:.3f}%'.format(round((over_N / N) * 100, 3)))       # :.3f 중요!!

    # :.3f -> {인덱스:0개수.자릿수f}