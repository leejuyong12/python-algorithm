def getMaxPos():
    maxV = COUNTS[0] # 일단 큰 값을 0번 위치 값으로 지정
    maxP = 0         # 큰 값의 인덱스는 0으로 일단 지정
    for i in range(1, len(COUNTS)):  # 1부터 끝까지 pos 값 반복
        if maxV <= COUNTS[i]:         # maxV 보다 COUNTS i위치의 값이 더 크면   <= 이러면 == 것도 처리해줌.
            maxV = COUNTS[i]         # maxV 값은 COUNTS i위치의 값으로 바뀐다.
            maxP = i                 # 그때의 pos는 i


    return maxP                      # maxP 를 리턴

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    CARDS = list(map(int, input()))

    # 카운트 정렬
    COUNTS = [0] * 10

    for i in range(N):          # COUNTS에 각각의 개수 입력
        p = CARDS[i]
        COUNTS[p] += 1

    pos = getMaxPos() # 최대값이 들어있는 위치를 구해서 최댓값과 위치를 return한다.

    print('#{} {} {}'.format(tc, pos, COUNTS[pos]))