import sys
sys.stdin = open('백준-시험 감독.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())    # 시험장의 개수
    A = list(map(int, input().split()))   # 각 시험장에 있는 응시자의 수
    B, C = map(int, input().split())
    # B = 총감독관이 한 시험장에서 감시할 수 있는 응시자의 수
    # C = 부 감독관이 한 시험장에서 감시할 수 있는 응시자의 수
    # 각각의 시험장에는 총 감독관이 오직 1명만 있어야 하고
    # 부감독관은 여러명 있어도 된다.
    # 필요한 감독관의 수의 최솟값 구하기
    total = 0
    total += N
    new_A = []
    for x in A:
        if x > B:
            new_A.append(x-B)

    for y in new_A:
        if y <= C:
            total += 1
        elif y > C:
            if y % C == 0:
                total += y // C
            else:
                total += (y // C) + 1
    print(total)
