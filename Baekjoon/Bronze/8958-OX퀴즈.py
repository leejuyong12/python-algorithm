import sys
sys.stdin = open('8958-백준-OX퀴즈.txt')

TC = int(input())

for tc in range(1, TC+1):
    check = list(input())

    score = 0
    score_p = 0

    for p in range(len(check)):
        if check[p] == 'O':
            score_p += 1
            score += score_p
        elif check[p] == 'X':
            score_p = 0
    print(score)
