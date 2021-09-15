
# 0번째는 [0, N-1]가장 큰값을 구해서 0번쨰의 데이터와 교환
# 1번째는 [1,N-1]가장 작은 값을 구해서 1번째의 데이터와 교환
# 2번째는 [2, N-1] 가장 큰 값을 구해서 2번째의 데이터와 교환
# i번째는 [i, N-1] i가 짝수일때는 가장 큰값을, 홀수일때는 가장 작은 값은 (1부터 시작하기)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    a = list(map(int, input().split()))

    for i in range(N): # index값으로 활용
        max_id = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if a[j] > a[max_id]:
                    max_id = j
            a[i], a[max_id] = a[max_id], a[i]
        elif i % 2 == 1:
            min_id = i
            for j in range(i+1, N):
                if a[j] < a[min_id]:
                    min_id = j
            a[i], a[min_id] = a[min_id], a[i]
    a = ' '.join(map(str, a[:10]))
    print('#{} {}'.format(tc, a))