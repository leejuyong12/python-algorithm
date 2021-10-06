N = int(input())

result = set()      # 똑같은 숫자가 들어오면 못받도록 set 활용

# 숫자를 안쓰면 0 , 쓰면 1 ~ N
for a in range(N+1):    # 첫번째 0 ~ N개 쓰고
    for b in range(N+1-a):  # 두번째 0 ~ N-a개
        for c in range(N+1-a-b):    # 세번째 0 ~ N-a-b개

            d = N - a - b - c       # 마지막은 0 ~ N-a-b-c개     # N = a + b + c + d

            total = a * 1 + b * 5 + c * 10 + d * 50     # a b c d 위치 상관 없음

            result.add(total)       # set 이니까 add

print(len(result))


