T = int(input())

for a in range(T):
    X, Y = map(int, input().split())
    print(f'#{a + 1} {X // Y} {X % Y}')