TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    total = 0  # 총 이익 넣을 공간
    max_price = prices[-1]  # 뒤부터 시작.(계산의 편리)
    for x in range(len(prices) - 2, -1, -1):
        if prices[x] < max_price:  # max_price 는 파는 가격! 이것보다 산 가격이 작으면 이익!
            total += max_price - prices[x]
        elif prices[x] > max_price:  # max_price 보다 큰 숫자가 나오면 그때 또 팔기!
            max_price = prices[x]
    print('#{} {}'.format(tc, total))