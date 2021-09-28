scores = list(map(int, input().split()))

scores.sort(reverse=True)

print(scores[1])
