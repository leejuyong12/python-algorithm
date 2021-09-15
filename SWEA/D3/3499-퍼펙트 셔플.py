TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    cards = input().split()
    deck = []

    idx = 1

    if N % 2 == 0:
        for i in range(N):
            if i < N // 2:
                deck.append(cards[i])
            else:
                deck.insert(idx, cards[i])
                idx += 2
    if N % 2 == 1:
        for j in range(N):
            if j < N // 2 + 1:
                deck.append(cards[j])
            else:
                deck.insert(idx, cards[j])
                idx += 2

    print('#{} {}'.format(tc, ' '.join(map(str, deck))))