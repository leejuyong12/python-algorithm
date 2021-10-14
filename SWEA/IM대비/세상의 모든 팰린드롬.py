import sys
sys.stdin = open('세상의 모든 팰린드롬.txt')

TC = int(input())
for tc in range(1, TC+1):
    text = list(input())


    for x in range(len(text)):
        if text[x] == '?':
            text[x] = text[-x-1]

    if text == text[::-1]:
        print('#{} {}'.format(tc, 'Exist'))
    else:
        print('#{} {}'.format(tc, 'Not exist'))
