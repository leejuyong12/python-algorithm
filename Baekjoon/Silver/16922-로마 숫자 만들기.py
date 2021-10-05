N = int(input())

result = set()

# 숫자를 안쓰면 0 , 쓰면 1 ~ N
for a in range(N+1):    # 첫번째 0 ~ N개 쓰고
    for b in range(N+1-a):  # 두번째 0 ~ N-a개
        for c in range(N+1-a-b):    # 세번째 0 ~ N-a-b개
            d = N - a - b - c       # 마지막은 0 ~ N-a-b-c개
            total = a * 1 + b * 5 + c * 10 + d * 50
            result.add(total)
print(len(result))


