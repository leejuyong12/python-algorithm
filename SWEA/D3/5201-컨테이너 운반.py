import sys
sys.stdin = open('컨테이너.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())

    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)

    j = 0
    sumV = 0
    for x in truck:
        while j < N and weight[j] > x:
            j += 1
        if j == N:
            break
        sumV += weight[j]
        j += 1
    print('#{} {}'.format(tc, sumV))
    # 컨테이너 , 트럭 용량을 각각 내림차순으로 정렬