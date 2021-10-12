import sys
sys.stdin = open('최빈수 구하기.txt')

TC = int(input())
for tc in range(1, TC+1):
    t = int(input())

    arr = list(map(int, input().split()))

    base = [0] * 101

    for x in range(len(arr)):
        base[arr[x]] += 1

    max_score_cnt = max(base)
    res = []
    for y in range(len(base)):
        if max_score_cnt == base[y]:
            res.append(y)
    print('#{} {}'.format(t, max(res)))