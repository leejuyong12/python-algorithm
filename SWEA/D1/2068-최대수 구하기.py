T = int(input())

for a in range(T):
    x = list(map(int, input().split()))

    print(f'#{a + 1} {max(x)}')