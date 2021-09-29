# tc = 3
# tc1 - N = 3 / 1 3 4  /        tc2 - N = 5 / 1 7 10 13 19
# tc3 - N = 3 / 1 500000000 999999999

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    num = [int(input()) for _ in range(N)]

    for x in range(0, len(num), )