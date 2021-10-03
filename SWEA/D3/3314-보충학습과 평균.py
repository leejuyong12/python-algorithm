TC = int(input())

for tc in range(1, TC+1):
    scores = list(map(int, input().split()))
    N = len(scores)
    total_scores = 0
    for sc in scores:
        if sc < 40:
            total_scores += 40
        else:
            total_scores += sc

    avg_score = total_scores // N
    print('#{} {}'.format(tc, avg_score))