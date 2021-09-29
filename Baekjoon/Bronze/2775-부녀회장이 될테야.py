TC = int(input())

for tc in range(1, TC+1):
    k = int(input())        # 층
    n = int(input())        # 호

    floor_0 = []
    for x in range(1, n+1):
        floor_0.append(x)

    for x in range(k):  # 각 층마다
        for y in range(1, n):       # 각 호에 사는 사람들 구하기
            floor_0[y] += floor_0[y-1]
    print(floor_0[-1])  # k개만큼이니까 층수에서 마지막을 구하면 된다.
    # result = 0
    # if k == 1:
    #     for x in range(1, n+1):
    #         result += x * (k)
    # elif k >= 2:
    #
    # print(result)