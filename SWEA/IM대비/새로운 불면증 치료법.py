import sys
sys.stdin = open('새로운 불면증 치료법.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    base = set()
    K = 1
    result = 0
    while True:
        for x in str(K*N):
            base.add(x)

        if len(base) == 10:
            result = K * N
            break
        K += 1

    print(result)
