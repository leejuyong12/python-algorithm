import sys
sys.stdin = open('초밥식사.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]
    # 우선순위는 a+b가 높은 순
    # a+b 순으로 정렬하려면 lambda 활용
    lst.sort(key=lambda sushi: sushi[0] + sushi[1], reverse=True)
    res_a = 0
    res_b = 0
    for x in range(N):
        if x % 2 == 0:
            res_a += lst[x][0]
        else:
            res_b += lst[x][1]
    print('#{} {}'.format(tc, res_a - res_b))
